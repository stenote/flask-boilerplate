from app import app


@app.cli.command('hello')
def hello():
    """hello world."""
    print("Hello World!")
