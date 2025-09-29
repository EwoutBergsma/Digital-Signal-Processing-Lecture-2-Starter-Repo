import pytest
from pathlib import Path
import pytest

CASE_FILES = sorted(Path("cases").glob("*.py"))

#@pytest.mark.parametrize("path", CASE_FILES, ids=lambda p: p.name)
