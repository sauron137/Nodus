class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns):
        if table_name in self.tables:
            return f"Error. table: '{table_name}' already exists"
        self.tables[table_name] = {"columns": columns, "rows": []}
        return f"Table '{table_name}' created."

    def insert(self, table_name, values):
        if table_name not in self.tables:
            return f"Error table '{table_name}' does not exist"

        table = self.tables[table_name]

        if len(values) != len(table["columns"]):
            return f"Error: expected {len(table['columns'])} values, got {len(values)}."

        row = dict(zip(table["columns"], values))
        table["rows"].append(row)
        return f"Row inserted into {table_name}."

    def get_table(self, table_name):
        if table_name not in self.tables:
            return None
        return self.tables[table_name]
