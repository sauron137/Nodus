from src.parser import parse, StatementType
from src.database import Database

db = Database()
db.load()



def handle_meta_command(command):
    if command == ".help":
        print("Meta-commands:")
        print(" .help – show this message")
        print(" .exit – quit the program")

    elif command == ".exit":
        print("Goodbye")
        return "exit"

    else:
        print(f"Unrecognized meta-command {command}")

def print_table(table):
    columns = table["columns"] 
    rows = table["rows"]

    if not rows:
        print("(Empty table)")
        return

    widths = []
    for col in columns:
        col_values = [str(row[col]) for row in rows]
        widths.append(max(len(col), max(len(v) for v in col_values)))

    header = " | ".join(col.ljust(widths[i]) for i, col in enumerate(columns)) 
    separator = "-+-".join("-" * widths[i] for i in range(len(columns)))

    print(header)
    print(separator)

    for row in rows: 
        line = " | ".join(str(row[col]).ljust(widths[i]) for i, col in enumerate(columns)) 
        print(line)

def handle_sql(statement):
    result = parse(statement)

    if result.statement_type == StatementType.CREATE_TABLE:
        message = db.create_table(result.table_name, result.columns)
        print(message)
    elif result.statement_type == StatementType.INSERT:
        message = db.insert(result.table_name, result.values)
        print(message)
    elif result.statement_type == StatementType.SELECT:
        table, error = db.select(result.table_name)
        print_table(table)
    else:
        print(f"Unrecognized SQL statement: {statement}")

def start_repl():
    print("SQLite Clone — type '.help' or '.exit' to get started.")

    while True:
        user_input = input("db > ").strip()

        if not user_input:
            continue

        if user_input.startswith("."):
            result = handle_meta_command(user_input.lower())
            if result == "exit":
                break

        else:
            handle_sql(user_input)

    db.save()


if __name__ == "__main__":
    start_repl()
