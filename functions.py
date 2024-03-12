FILEPATH = 'todo.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(action, todo_name=None, lst_name=None, filepath=FILEPATH):
    """
    :param lst_name: new list to rewrite the file
    :param todo_name: name of the to_do you want to add
    :param action: either a : to append to_do to the current list or w : to rewrite the whole file again .
    """
    match action:
        case 'a':
            with open(filepath, 'a') as file_local:
                file_local.write(todo_name.title())
        case 'w':
            with open(filepath, 'w') as file_local:
                file_local.writelines(lst_name)
