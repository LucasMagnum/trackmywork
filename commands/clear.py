import click

from core import storage


@click.command()
def command():
    """Clear command"""
    click.confirm('Do you want delete all the records?', abort=True)

    storage.clear()
