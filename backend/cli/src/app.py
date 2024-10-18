import click
from rich import print
from zotero.api import Zotero


@click.group()
def cli():
    """
    A simple CLI to interact with the zotero app.
    """
    pass


@click.command()
def collections():
    """
    List all collections
    """
    zotero = Zotero()
    collection_list = zotero.get_collections()
    collections = [collection.data.name for collection in collection_list]
    print("[bold]Available collections:[/bold]")
    for collection in collections:
        print(f"[italic green]- {collection}[/italic green]")


cli.add_command(collections)

if __name__ == "__main__":
    cli()
