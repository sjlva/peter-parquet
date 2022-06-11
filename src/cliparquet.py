import pyarrow.parquet as pq

class CLIParquet:
    def __init__(self, parquet_path, column = None):
        self.table = pq.read_table(parquet_path)
        self.file = pq.ParquetFile(parquet_path)

        if column is not None:
            self.column_index = self.table.column_names.index(column)
        else:
            self.column_index = None
            
    def metadata(self): 
        if self.column_index is not None:
            return self.file.metadata.row_group(0).column(self.column_index)
        else:
            return self.file.metadata

    def head(self, n = 5):
        if self.column_index is not None:
            return self.table.column(self.column_index)[0:n].to_pylist()
        else:
            return self.table[0:n].to_pylist()

    def tail(self, n = 5):
        if self.column_index is not None:
            return self.table.column(self.column_index)[-n:].to_pylist()
        else:
            return self.table[-n:].to_pylist()

    def cat(self):
        if self.column_index is not None:
            return self.table.column(self.column_index).to_pylist()
        else:
            return self.table.to_pylist()

    def schema(self):
        return self.table.schema

    def not_null(self) -> bool: 
        if self.column_index is None:
            print("Feature only available for single column.")
            return None
        else:
            not_null = True if self.table[self.column_index].null_count == 0 else False 
            return not_null

    def is_unique(self) -> bool:
        if self.column_index is None:
            print("Feature only available for single column.")
            return None
        else:
            total_rows = len(self.table[self.column_index])
            unique_rows = len(self.table[self.column_index].unique())
            return total_rows == unique_rows
