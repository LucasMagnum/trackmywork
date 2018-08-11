import click

from core import storage
from . import options


@click.command()
@options.message
@options.time
@options.project
@options.category
@options.links
def command(message, time, project, category, links):
    """
    Use this command to register a task without tracking the start and finish time.

    $ trackmywork register -m "Starting my task" -p "trackmywork" -c "personal" -t 2h

    The task 1 - "Starting my task" was registered with success.
    """
    task = storage.register(
        message=message,
        time=time,
        project=project,
        category=category,
        links=links,
    )

    click.echo(f'The task {task.id} - "{task.message}" was registered with success.')
