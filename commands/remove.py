import click

from core import storage


@click.command()
@click.argument('task_id', type=str)
def command(task_id):
    """
    Use this command to remove a specified task.

    $ trackmywork remove 3
    Do you want to remove the task 3? [yn]

    The task 3 was removed with success.
    """
    click.confirm(f'Do you want remove the task {task_id}?', abort=True)

    storage.remove(task_id)

    click.echo(f"The task {task_id} was removed with success.")
