FILEPATH="todos.txt"


def get_todos(filepath=FILEPATH):
    """"Read the text file and return the list of todo items"""
    with open(filepath,'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local



def write_todos(todos_arg,filepath=FILEPATH):
    """Write the todo items in the text file"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
        



