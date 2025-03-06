import os
from pathlib import Path
import shutil
import pytest


@pytest.fixture(scope="function")
def test_dir():
    """Fixture that creates a temporary test directory and ensures cleanup after tests."""
    base_test_dir = Path(__file__).parent / "test_data"
    
    # Remove old test data
    shutil.rmtree(base_test_dir, ignore_errors=True)
    
    # Create fresh test directories
    os.makedirs(base_test_dir / "output", exist_ok=True)
    
    yield base_test_dir  # Provide the test directory to tests
    
    # Cleanup after test completes
    shutil.rmtree(base_test_dir, ignore_errors=True)