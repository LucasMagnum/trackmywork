import click

from core import storage
from . import options


@click.command()
@click.argument('task_id', type=str)
@click.option('--message', '-m', help='activity message')
@click.option('--time', '-t', help='activity time (hours)')
@options.project
@options.category
@options.links
def command(task_id, message, time, project, category, links):
    """
    Use this command to edit a task.

    $ trackmywork edit 2 -m "Changing the task message" -t 3h -l ""
    The task 2 was edited with success. Fields changed: [message, time, links]
    """
    task_id, fields_changed = storage.edit(
        task_id, message, time, project, category, links
    )

    if not fields_changed:
        click.echo(f"No changes made to task {task_id}.")
        return

    click.echo(
        f"The task {task_id} was edited with success."
        f"Fields changed: {fields_changed}"
    )
