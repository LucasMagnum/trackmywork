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
    $ trackmywork start -m "Starting my task" -p "trackmywork" -c "personal" -t 2h

    You successfully started the task 1 - "Starting my task"

    # Adding links to a task

    $ trackmywork start -m "Task with links" -l "http://google.com" -t 2h

    You successfully started the task 2 - "Task with links"
    """
    task = storage.save(
        message=message,
        time=time,
        project=project,
        category=category,
        links=links,
    )

    click.echo(f'You successfully started the task #{task.id} - "{task.message}"')
