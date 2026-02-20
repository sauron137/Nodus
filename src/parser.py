class StatementType:
    CREATE_TABLE = "CREATE_TABLE"
    INSERT = "INSERT"
    SELECT = "SELECT"
    UNKNOWN = "UNKNOWN"

class Statement:
    def __init__(self, statement_type, table_name=None, columns=None, values=None):
        self.statement_type = statement_type
        self.table_name = table_name
        self.columns = columns
        self.values = values

def parse(user_input):
    uppercased = user_input.strip().upper()

    if uppercased.startswith("CREATE TABLE"):
        return parse_create_table(user_input)
    elif uppercased.startswith("INSERT INTO"):
        return parse_insert(user_input)
    elif uppercased.startswith("SELECT"):
        return parse_select(user_input)
    else:
        return Statement(StatementType.UNKNOWN)

def parse_create_table(user_input):
    try:
        after_keyword = user_input.strip()[len("CREATE TABLE"):].strip()
        paren_open = after_keyword.index("(")
        paren_close = after_keyword.index(")")
        table_name = after_keyword[:paren_open].strip()
        columns_raw = after_keyword[paren_open + 1:paren_close]
        columns = [col.strip() for col in columns_raw.split(",")]
        return Statement(StatementType.CREATE_TABLE, table_name=table_name, columns=columns)
    except ValueError:
        return Statement(StatementType.UNKNOWN)

def parse_insert(user_input):
    try:
        after_keyword = user_input.strip()[len("INSERT INTO"):].strip()
        paren_open = after_keyword.index("(")
        paren_close = after_keyword.index(")")
        table_name = after_keyword[:paren_open].strip()
        values_raw = after_keyword[paren_open + 1:paren_close]
        values = [val.strip() for val in values_raw.split(",")]
        return Statement(StatementType.INSERT, table_name=table_name, values=values)
    except ValueError:
        return Statement(StatementType.UNKNOWN)

def parse_select(user_input):
    try:
        uppercased = user_input.strip().upper()
        from_index = uppercased.index("FROM")
        table_name = user_input[from_index + len("FROM"):].strip()
        table_name = table_name.rstrip(";").strip()
        return Statement(StatementType.SELECT, table_name=table_name)
    except ValueError:
        return Statement(StatementType.UNKNOWN)
