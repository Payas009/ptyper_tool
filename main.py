import typer  # Bring in the Typer toolkit

app = typer.Typer()  # Create the main app to manage our commands

@app.command()  # Tell Typer this is a command
def hello(name: str):  
    print(f"Hello {name}")

@app.command()  # Another command!
def goodbye(name: str, formal: bool = False):
    if formal:  # Check if the "--formal" flag is used
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:  # Casual goodbye
        print(f"Bye {name}!")


@app.command()  # Another command!
def curse(name: str, bad: bool = False):
    if bad:  # Check if the "--bad" flag is used
        typer.echo(f"You are a bad person, {name}.")
    else:  # Informal curse
        typer.echo(f"You have a tiny dick, you jerk. Go away, {name}!")


if __name__ == "__main__":
    app()  # Run the app with all its commands