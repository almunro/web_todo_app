FILEPATH = "todos.txt"


#def get_todos(filepath="todos.txt"):
    # we can change the above line of code by adding FILEPATH = "todos.txt" at the top of the page and then recoding anything in the function that has filepath="todos.txt" to filepath=FILEPATH
# def get_todos(filepath=FILEPATH):

def get_todos(filepath=FILEPATH):
    """ Open a text file and read a list of items in the file """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


#def write_todos(todos_arg, filepath=todos.txt):
   # """ Write the new to do items list to the text file """
   # with open(filepath, "w") as file_local:
   #     file_local.writelines(todos_arg)


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the new to do items list to the text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)



if __name__ == "__main__":
    print("Hello")
    print(get_todos())
