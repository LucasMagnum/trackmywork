import click

from core import config, storage
from core.task import Task


@click.command()
@click.option('--message', '-m', prompt='Message', help='activity message')
@click.option('--time', '-t', prompt='Time', help='activity time (hours)')
@click.option('--project', '-p', default=config.DEFAULT_PROJECT, help='project this activity belongs to')
@click.option('--category', '-c', default=config.DEFAULT_CATEGORY, help='category this activity belongs to')
@click.option('--links', '-l', help='links related to this activity')
def command(message, time, project, category, links):
    """
    Use this command to register a task without tracking the start and finish time.

    $ trackmywork register -m "Starting my task" -p "trackmywork" -c "personal" -t 2h

    The task 1 - "Starting my task" was registered with success.
    """
    task = Task.create(
        message=message,
        time=time,
        category=category,
        links=links,
        project=project
    )
    task.start()
    task.finish()

    task = storage.save(task)

    click.echo(f'The task {task.id} - "{task.message}" was registered with success.')
