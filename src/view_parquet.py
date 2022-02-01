from rich_dataframe import prettify
import pyarrow.parquet as pq
import pandas as pd
import click

def parquet_to_pandas(file):
    table = pq.read_table(file)
    df = table.to_pandas()
    df = df.T
    return df

def parse_df(df, rows, cols):
    parsed_table = prettify(df, row_limit = cols, col_limit = rows, clear_console = True)
    return parsed_table

@click.command()
@click.argument('file')
@click.option('--rows', default=10, help='Number of rows to display')
@click.option('--cols', default=20, help = 'Number of columns to display')
def main(file, rows, cols):
    df = parquet_to_pandas(file)
    parsed_table = parse_df(df, rows, cols)
    click.echo(parsed_table)

if __name__ == "__main__":
    main()
