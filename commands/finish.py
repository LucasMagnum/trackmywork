import click
import sys

from core import storage


@click.command()
@click.argument('task_id', type=str, required=False)
def command(task_id):
    """
    Use this command to finish a task.
    This will add the `finished_at` metadata to your task.

    $ trackmywork finish
    The last task 3 was finished with success.

    $ trackmywork finish 2
    The task 2 was finished with success.

    $ trackmywork finish 2
    The task 2 is already finished.
    """
    task = storage.get_by_id(task_id) if task_id else storage.get_latest()

    if not task:
        click.echo(f"Task {task_id} not found.")
        sys.exit(1)

    finished = task.finish()

    if not finished:
        already_finished_message = (
            f"The {'' if task_id else 'last '}task {task.id} is already finished."
        )
        click.echo(already_finished_message)
        sys.exit(1)

    storage.save(task)
    success_message = (
        f"The {'' if task_id else 'last '}task {task.id} was finished with success."
    )
    click.echo(success_message)
