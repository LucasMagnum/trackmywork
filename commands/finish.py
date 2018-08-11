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
    if not task_id:
        task = storage.finish_last_task()

        click.echo(f"You successfully finished the last task {task.id}")
    else:
        task = storage.finish_task(task_id)
        click.echo(f"You successfully finished the task '{task.id}'.")
