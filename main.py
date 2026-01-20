from typer import Typer

cmd = Typer()


@cmd.command()
def test1():
    print("Hello from test1")


@cmd.command()
def test2():
    print("Hello from test2")


if __name__ == "__main__":
    cmd()
