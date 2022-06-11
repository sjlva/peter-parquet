import typer
from rich.console import Console
from rich.table import Table
from peter_parquet.cliparquet import CLIParquet

console = Console()
app = typer.Typer()

@app.command()
def schema(file: str = typer.Option(..., "--file", "-f")):
    peter = CLIParquet(parquet_path=file)
    console.print(peter.schema())
    
@app.command()
def metadata(file: str = typer.Option(..., "--file", "-f"),
             column: str = typer.Option(None, "--column", "-c")):
    peter = CLIParquet(parquet_path=file, column=column)
    console.print(peter.metadata())

@app.command()
def head(file: str = typer.Option(..., "--file", "-f"),
         column: str = typer.Option(None, "--column", "-c"),
         n: int = typer.Option(5, "--nrows", "-n")):
    peter = CLIParquet(parquet_path=file, column=column)
    console.print(peter.head(n))

@app.command()
def tail(file: str = typer.Option(..., "--file", "-f"),
         column: str = typer.Option(None, "--column", "-c"),
         n: int = typer.Option(5, "--nrows", "-n")):
    peter = CLIParquet(parquet_path=file, column=column)
    console.print(peter.tail(n))

@app.command()
def cat(file: str = typer.Option(..., "--file", "-f"),
        column: str = typer.Option(None, "--column", "-c")):
    peter = CLIParquet(parquet_path=file, column=column)
    console.print(peter.cat())

@app.command()
def not_null(file: str = typer.Option(..., "--file", "-f"),
        column: str = typer.Option(None, "--column", "-c")):
    peter = CLIParquet(parquet_path=file, column=column)
    console.print(peter.not_null())

@app.command()
def is_unique(file: str = typer.Option(..., "--file", "-f"),
        column: str = typer.Option(None, "--column", "-c")):
    peter = CLIParquet(parquet_path=file, column=column)
    console.print(peter.is_unique())





if __name__ == "__main__":
    app()
