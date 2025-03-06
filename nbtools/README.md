# nbtools

`nbtools` is a Python library for rendering **Mermaid.js** and **Graphviz** diagrams inside Jupyter Notebooks.

## 📦 Installation
```sh
pip install -e .
```
> Make sure you have `graphviz` installed on your system:
```sh
sudo apt install graphviz  # Ubuntu/Debian
brew install graphviz      # macOS
choco install graphviz     # Windows
```

## 🚀 Features
- **Render Mermaid.js diagrams** inside Jupyter Notebooks
- **Display Graphviz graphs** with automatic rendering
- **export notebook cells** to png files

## 🔧 Usage

### **Mermaid**
Render a graph using the `mermaid` library in the output of a notebook cell.

<p align="center">
  <img src="..\slideshows\images\construct_chart_Cell1.png" 
       alt="Rendered Chart"
       style="border: 2px solid #ddd; border-radius: 10px; box-shadow: 4px 4px 10px rgba(0,0,0,0.2); width: 80%;">
</p>


### **Graphviz**
Render a graph using the `graphviz` library in the output of a notebook cell.

<p align="center">
  <img src="..\slideshows\images\construct_chart_Cell2.png" 
       alt="Rendered Chart"
       style="border: 2px solid #ddd; border-radius: 10px; box-shadow: 4px 4px 10px rgba(0,0,0,0.2); width: 80%;">
</p>

### export cells
Output to a folder a representation of all cells tagged with `export` in the notebook.
<p align="center">
  <img src="..\slideshows\images\construct_chart_Cell4.png" 
       alt="Rendered Chart"
       style="border: 2px solid #ddd; border-radius: 10px; box-shadow: 4px 4px 10px rgba(0,0,0,0.2); width: 80%;">
</p>


