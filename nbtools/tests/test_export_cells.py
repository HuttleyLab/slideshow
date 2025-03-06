import nbformat
from nbtools import export_cells  # Import from package

def create_test_notebook(path):
    """Create a minimal Jupyter Notebook with a tagged cell."""
    nb = nbformat.v4.new_notebook()
    nb.cells.append(nbformat.v4.new_markdown_cell("# This is a normal markdown cell"))
    nb.cells.append(nbformat.v4.new_code_cell("print('Hello, world!')", metadata={"tags": ["export"]}))
    
    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

def test_extract_and_render_cells(test_dir):
    """Test that extracting and rendering notebook cells creates image files."""
    notebook_path = test_dir / "test_notebook.ipynb"
    output_dir = test_dir / "output"
    
    create_test_notebook(notebook_path)
    export_cells(str(notebook_path), str(output_dir))  # Now using library-level function

    # Ensure an image file was created
    image_files = list(output_dir.glob("*.png"))
    assert len(image_files) > 0, "No images were generated from tagged cells."
