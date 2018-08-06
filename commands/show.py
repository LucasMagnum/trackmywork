import click

from core import storage


class ClickStdoutAdapter:
    def write(self, string):
        click.echo(string)


@click.command()
@click.argument('task_id', type=str, required=False)
@click.option('--tail', is_flag=True, help='Show logs in reverse order')
@click.option('--limit', type=int, default=10, help='Define the limit of tasks')
def command(task_id, tail, limit):
    """Show command"""
    stdout_adapter = ClickStdoutAdapter()

    if task_id:
        storage.show_task(stdout_adapter, task_id)
    else:
        storage.show_all(stdout_adapter, tail=tail, limit=limit)
