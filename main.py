from commands import clear, edit, finish, register, remove, show, start

import click


@click.group()
def cli():
    """
    Trackmywork is an application to help us keep track of our
    tasks in a simple way using the command line.

    One of the good habits of productivity is to keep track of every task we do
    and this application will help us to do it :)

    # Default configurations

    export TRACKMYWORK_DEFAULT_CATEGORY="work"

    export TRACKMYWORK_DEFAULT_PROJECT="myproject"

    So, we could set up a default category or project.
    When no `category` is given, it will use the `TRACKMYWORK_DEFAULT_CATEGORY`
    if it exists, the same for `project`.
    """
    pass


cli.add_command(clear.command, name="clear")
cli.add_command(edit.command, name="edit")
cli.add_command(finish.command, name="finish")
cli.add_command(register.command, name="register")
cli.add_command(remove.command, name="remove")
cli.add_command(show.command, name="show")
cli.add_command(start.command, name="start")


if __name__ == '__main__':
    cli()
