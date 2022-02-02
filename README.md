# Peter Parquet
Quickly inspect parquet files in command line

<img title="a title" alt="Alt text" src="https://i.imgur.com/gjKIEl6.png">

## Installation

```bash
pip install peter-parquet
```


## Usage

```bash
Usage: view_parquet [OPTIONS] FILE

Options:
  --rows INTEGER  Number of rows to display
  --cols INTEGER  Number of columns to display
  --help          Show this message and exit
```

## Usage Examples 

### View local parquet file

```bash
view_parquet path/to/parquet/file.parquet
```

## Non Bash users

If you are a non Bash user, notice that Python package executables are installed to ~/.local/bin. So, make sure to add this entry to your PATH variable.

### ZSH

Actually, using ZSH allows you to use special mapping of environment variables. So you can simply do:

```bash
path+=$HOME/.local/bin:$PATH
export PATH
```


