import click

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
    if task_id:
        _, finished = storage.finish_task(task_id)
        message = ''
    else:
        message = 'last '
        task_id, finished = storage.finish_last_task()

    if not finished:
        click.echo(f"The {message}task {task_id} is already finished.")
        return

    click.echo(f"The {message}task {task_id} was finished with success.")
