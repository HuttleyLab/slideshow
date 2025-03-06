import asyncio
import os
import uuid
import warnings
import nbformat
import nbformat.v4 as nbf
from nbconvert import HTMLExporter
from pathlib import Path
from playwright.async_api import async_playwright
from nbformat.validator import MissingIDFieldWarning

# Try to detect if we are inside a Jupyter Notebook
try:
    from IPython import get_ipython
    in_jupyter = get_ipython() is not None
    if in_jupyter:
        import nest_asyncio
        nest_asyncio.apply()  # Apply patch to allow nested async loops
except ImportError:
    in_jupyter = False  # Not in Jupyter
    
async def render_html_to_image(html_content, image_path):
    """Render HTML to an image using Playwright."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        await page.screenshot(path=image_path, full_page=True)
        await browser.close()

async def process_cells_async(notebook_path, output_dir, tag="export"):
    """Extracts tagged cells from a notebook and renders them as images."""


    with warnings.catch_warnings():
        warnings.simplefilter("ignore", MissingIDFieldWarning)  # VS Code makes ipynb's without ids
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)

        # Extract tagged cells
        tagged_cells = [
            (idx, cell) for idx, cell in enumerate(notebook.cells)
            if "metadata" in cell and "tags" in cell.metadata and tag in cell.metadata["tags"]
        ]

        html_exporter = HTMLExporter()
        notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]  # Strip .ipynb extension
        tasks = []

        for cell_idx, cell in tagged_cells:
            # Create a minimal NotebookNode
            temp_notebook = nbf.new_notebook(cells=[cell])

            # Convert to HTML
            html_content, _ = html_exporter.from_notebook_node(temp_notebook)
            image_filename = f"{notebook_name}_Cell{cell_idx}.png"
            image_path = os.path.join(output_dir, image_filename)

            # Provide feedback before processing
            print(f"💾 Saving: {image_path}", flush=True)

            # Schedule rendering as an async task
            tasks.append(render_html_to_image(html_content, image_path))
    
    await asyncio.gather(*tasks)

def export_cells(notebook_path, output_dir):
    """Handles running the async rendering process properly."""
    print(f"💻 Processing: {notebook_path}", flush=True)
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook not found: {notebook_path}")
    
    os.makedirs(output_dir, exist_ok=True)

    try:
        loop = asyncio.get_running_loop()
        task = loop.create_task(process_cells_async(notebook_path, output_dir))
        loop.run_until_complete(task)
    except RuntimeError:
        asyncio.run(process_cells_async(notebook_path, output_dir))
