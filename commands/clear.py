import click

from core import storage


@click.command()
def command():
    """
    Use this command to clear all the tasks from the storage.

    $ trackmywork clear
    All tasks were deleted successfully.
    """
    click.confirm('Are you sure about this?', abort=True)

    storage.clear()
    click.echo('All tasks were deleted successfully.')
