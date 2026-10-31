# while True:  # always True to infinite loop
#     print("hello")

user_prompt = "Enter a todo:"
todos = []  # empty list

while True:  # this will always be true, True is a BOOLEAN Datatype
    todo = input(user_prompt)
    print(todo.title())  # .title capitalizes each letter
    todos.append(todo)
