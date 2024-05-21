"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Toytoy."""


if __name__ == "__main__":
    main(prog_name="toytoy")  # pragma: no cover
