import graphviz
from IPython.display import Image, display

def display_graphviz(graph):
    """Render and display a Graphviz graph within a Jupyter Notebook."""
    # Render the graph to a file (SVG or PNG can be used here)
    # Note: You might need to adjust the directory path or ensure it exists
    filename = graph.render(filename='temp_graph', format='png', cleanup=True)
    # Display the image in the notebook
    display(Image(filename))

def gv(graph):
    """Given a string containing a Graphviz-format graph, display it."""
    graph = graphviz.Source(graph)
    display_graphviz(graph)