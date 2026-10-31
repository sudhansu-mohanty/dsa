user_prompt = "Enter a todo:"
todos = []  # empty list

while True:  # this will always be true, True is a BOOLEAN Datatype
    todo = input(user_prompt)
    todo_capitalize = todo.capitalize()
    todos.append(todo)  # todo is appended in todosmega-course
    print(todos)
