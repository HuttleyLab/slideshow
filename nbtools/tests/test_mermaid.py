import pytest
from nbtools import mm

def test_mm():
    """Ensure mm does not raise errors."""
    mermaid_code = "graph TD; A-->B; A-->C; B-->D; C-->D;"
    try:
        mm(mermaid_code)
    except Exception as e:
        pytest.fail(f"mm raised an error: {e}")

