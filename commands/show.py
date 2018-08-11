import click

from core import storage


class ClickStdoutAdapter:
    def write(self, string):
        click.echo(string)


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
    stdout_adapter = ClickStdoutAdapter()

    if task_id:
        storage.show_task(stdout_adapter, task_id)
    else:
        storage.show_all(stdout_adapter, tail=tail, wip=wip, limit=limit)
