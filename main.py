user_prompt = "Enter a todo:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize()) #capitalize kelimenin veya cümlenin yalnızca ilk harfini büyük yapar, title cümledeki tüm kelimelerin ilk harfini büyük yapar.
    todos.append(todo)