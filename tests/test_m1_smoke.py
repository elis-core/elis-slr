"""M1 smoke tests: package import, CLI help, module execution."""

import subprocess
import sys


def test_import_elis_slr():
    """Test that the elis_slr package can be imported."""
    import elis_slr  # noqa: F401


def test_import_version():
    """Test that __version__ is accessible."""
    from elis_slr import __version__  # noqa: F401

    assert __version__ == "2.0.0"


def test_cli_help():
    """Test that elis-slr --help exits cleanly."""
    result = subprocess.run(
        [sys.executable, "-m", "elis_slr", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Usage:" in result.stdout or "usage:" in result.stdout
    assert "elis-slr" in result.stdout


def test_cli_version():
    """Test that elis-slr --version prints the version."""
    result = subprocess.run(
        [sys.executable, "-m", "elis_slr", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "2.0.0" in result.stdout


def test_module_execution():
    """Test that python -m elis_slr works (no args, should print help)."""
    result = subprocess.run(
        [sys.executable, "-m", "elis_slr"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Usage:" in result.stdout