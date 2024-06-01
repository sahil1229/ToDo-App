
def get_todos(address="data.txt"):
    """Read a text file
    and return list of todos"""
    with open(address, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, address="data.txt",):
    """write the todo items in a text file"""
    with open(address, "w") as file:
        file.writelines(todos_arg)

