import click


@click.command("hello")
def hello():
    """hello world."""
    print("Hello World!")
