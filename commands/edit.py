import sys

import click

from core import storage


@click.command()
@click.argument('task_id', type=str)
@click.option('--message', '-m', help='activity message')
@click.option('--time', '-t', help='activity time (hours)')
@click.option('--project', '-p', help='project this activity belongs to')
@click.option('--category', '-c', help='category this activity belongs to')
@click.option('--links', '-l', help='links related to this activity')
def command(task_id, message, time, project, category, links):
    """
    Use this command to edit a task.

    $ trackmywork edit 2 -m "Changing the task message" -t 3h -l ""
    The task 2 was edited with success. Fields changed: [message, time, links]
    """
    task = storage.get_by_id(task_id)

    if not task:
        click.echo(f"Task {task_id} not found.")
        sys.exit(1)

    new_values = {
        'message': message,
        'time': time,
        'project': project,
        'category': category,
        'links': links,
    }

    fields_changed = task.edit(new_values)

    if not fields_changed:
        click.echo(f"No changes made to the task {task.id}.")
        sys.exit(1)

    storage.save(task)

    fields_name = [field_name for field_name, *_ in fields_changed]
    click.echo(
        f"The task {task_id} was edited with success. "
        f"Fields changed: {fields_name}"
    )
