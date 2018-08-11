import sys

import click

from core import storage


@click.command()
@click.argument('task_id', type=str, required=False)
@click.option('--tail', is_flag=True, help='Show tasks in reverse order')
@click.option('--wip', is_flag=True, help='Show only uncompleted tasks')
@click.option('--limit', type=int, default=10, help='Define the limit of tasks')
def command(task_id, tail, wip, limit):
    """
    Use this command to show a task or all the tasks.

    $ trackmywork show
    id;time;project;category;links;started_at;finished_at
    1;Starting a new task;2h;trackmywork;personal;;2018-08-11 14:41:39.584405;
    2;Starting a second task;2h;trackmywork;personal;;2018-08-11 14:41:39.584405;

    $ trackmywork show 1
    id;time;project;category;links;started_at;finished_at
    1;Starting a new task;2h;trackmywork;personal;;2018-08-11 14:41:39.584405;

    $ trackmywork show --tail --limit 1
    id;time;project;category;links;started_at;finished_at
    2;Starting a new task;2h;trackmywork;personal;;2018-08-11 14:41:39.584405;
    """
    if task_id:
        task = storage.get_by_id(task_id)

        if not task:
            click.echo(f"Task {task_id} not found.")
            sys.exit(1)

        tasks = [task]
    else:
        tasks = storage.all(limit=limit, reverse=tail, wip=wip)

    print_header()
    for task in tasks:
        show_task(task)


def show_task(task, sep=';'):
    template = (
        f"{task.id}{sep}{task.message}"
        f"{sep}{task.time}"
        f"{sep}{task.project or ''}"
        f"{sep}{task.category or ''}"
        f"{sep}{task.links or ''}"
        f"{sep}{task.started_at or ''}"
        f"{sep}{task.finished_at or ''}"
    )

    click.echo(template)


def print_header(sep=';'):
    header = ('id', 'time', 'project', 'category', 'links', 'started_at', 'finished_at')
    click.echo(sep.join(header))
