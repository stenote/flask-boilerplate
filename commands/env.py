import os
import click

from app import app


@app.cli.command('env')
@click.argument('var')
def env(var):
    print(os.getenv(var, None))
