import click

from . import options


@click.command()
@options.message
@options.time
@options.project
@options.category
@options.links
def command(message, time, project, category, links):
    """
    $ trackmywork start -m "Starting my task" -p "trackmywork" -c "personal" -t 2h

    You successfully started the task #01 - "Starting my task"

    # Adding links to a task

    $ trackmywork start -m "Task with links" -l "http://google.com" -t 2h

    You successfully started the task #02 - "Task with links"
    """
    click.echo("Start command")
    click.echo(f'You successfully started the task #01 - "{message}"')
    click.echo("%s, %s, %s, %s" % (time, project, category, links))
