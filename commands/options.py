import click

from core import config


message = click.option('--message', '-m', prompt='Message', help='activity message')
time = click.option('--time', '-t', prompt='Time', help='activity time (hours)')
project = click.option('--project', '-p', default=config.DEFAULT_PROJECT,
                       help='project this activity belongs to')
category = click.option('--category', '-c', default=config.DEFAULT_CATEGORY,
                        help='category this activity belongs to')
links = click.option('--links', '-l', help='links related to this activity')
