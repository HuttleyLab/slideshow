from nbtools import gv
import pytest

def test_gv():
    """Ensure gv function does not raise errors."""
    graphviz_code = """
    digraph G {
        A -> B;
        A -> C;
        B -> D;
        C -> D;
    }
    """
    try:
        gv(graphviz_code)
    except Exception as e:
        pytest.fail(f"gv raised an error: {e}")
