import click


@click.command()
@click.argument('activity_id', required=False)
def command(activity_id):
    """
    We should save when we `finish` the task,
    that way is possible to keep track of the time it took between the `start` and `finish`.

    $ trackmywork finish

    You successfully finished the last task #02

    $ trackmywork finish #02

    You successfully finished the task #02
    """
    if not activity_id:
        click.echo("You successfully finished the last task #02")
    else:
        click.echo(f"You successfully finished the task '{activity_id}'.")
