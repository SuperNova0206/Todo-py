# tests/test_todopy.py

from typer.testing import CliRunner

from todopy import __app_name__, __version__, cli

runner = CliRunner()

def test_version() -> None : 
	result = runner.invoke(cli.app, ["--version"])
	assert result.exit_code == 0
	assert f"{__app_name__} v{__version__}" == result.stdout.strip()