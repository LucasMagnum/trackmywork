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

    You successfully registered the task 1 - "Starting my task"
    """
    task = storage.register(
        message=message,
        time=time,
        project=project,
        category=category,
        links=links,
    )

    click.echo(f'You successfully registered the task {task.id} - "{task.message}"')
