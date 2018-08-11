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
    Use this command to start a new task, this command will track
    when the task started and this information as a metadata of your task.

    $ trackmywork start -m "Starting my task" -p "trackmywork" -c "personal" -t 2h

    You successfully started the task 1 - "Starting my task"

    # Adding links to a task

    $ trackmywork start -m "Task with links" -l "http://google.com" -t 2h

    The task 2 - "Task with links" was started with success.
    """
    task = storage.save(
        message=message,
        time=time,
        project=project,
        category=category,
        links=links,
    )

    click.echo(f'The task {task.id} - "{task.message}" was started with success')
