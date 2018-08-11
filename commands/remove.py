import click

from core import storage


@click.command()
@click.argument('task_id', type=str)
def command(task_id):
    """Remove command"""
    click.confirm(f'Do you want delete the task_id {task_id}?', abort=True)

    storage.remove(task_id)

    click.echo(f"Task {task_id} removed with success.")
