"""This module provides the todopy CLI"""
# todopy/clip.py
from typing import Optional

import typer

from todopy import __app_name__, __version__

# initiat the app
app = typer.Typer()

# Display app version
def _version_callback(value : bool) -> None :
	if value:
		typer.echo(f"{__app_name__} v{__version__}")
		raise typer.Exist()

# Main func 
@app.callback()
def main(
		version : Optional[bool] = typer.Option(
			None, 
			"--version",
			"-v",
			help="shows the application's version and exit.",
			callback=_version_callback,
			is_eager=True,
		)
	) -> None : return

