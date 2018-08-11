import click


@click.command()
def command():
    """
    Use this command to edit a task.

    $ trackmywork edit 2 -m "Changing the task message" -t 3h -l ""
    You edited the task 2 changed message, time and links.
    """
    click.echo("You edited the {task_id}")
