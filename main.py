from parser import parse, StatementType
from database import Database

db = Database()



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

def handle_sql(statement):
    result = parse(statement)

    if result.statement_type == StatementType.CREATE_TABLE:
        message = db.create_table(result.table_name, result.columns)
        print(message)
    elif result.statement_type == StatementType.INSERT:
        message = db.insert(result.table_name, result.values)
        print(message)
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


if __name__ == "__main__":
    start_repl()
