import click

from core import storage


@click.command()
@click.argument('task_id', type=str, required=False)
def command(task_id):
    """
    Use this command to finish a task.
    This will add the `finished_at` metadata to your task.

    $ trackmywork finish

    You successfully finished the last task 2

    $ trackmywork finish 2

    You successfully finished the task 2
    """
    if task_id:
        _, finished = storage.finish_task(task_id)
    else:
        task_id, finished = storage.finish_last_task()

    if not finished:
        click.echo(f"The task {task_id} is already finished")
        return

    click.echo(f"The task {task_id} was finished with success.")
