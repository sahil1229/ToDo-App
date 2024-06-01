import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is, {now}")

while True:
    user_action = input("Add, Show, Edit, Complete or Exit: ")

    if user_action.startswith("add"):
        inputs = user_action[4:]
        todos = functions.get_todos("data.txt")
        todos.append(inputs + '\n')
        functions.write_todos(todos, "data.txt")

    elif user_action.startswith("show"):
        todos = functions.get_todos("data.txt")
        new_todo = []
        new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index+1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number-1
            todos = functions.get_todos("data.txt")
            temp_var = todos[number]
            temp_var = temp_var.strip("\n")
            print(temp_var)

            todos[number] = input("Enter the new task: ") + "\n"
            functions.write_todos(todos, "data.txt")

        except ValueError:
            print("Command not valid. Please enter edit followed by the number")
            continue

    elif user_action.startswith("complete"):
        try:
            toRemove = int(user_action[9:])
            toRemove = toRemove-1

            todos = functions.get_todos("data.txt")

            temp_var = todos[toRemove]
            todos.pop(toRemove)
            temp_var = temp_var.strip("\n")

            functions.write_todos(todos, "data.txt")

            print(f"The todo {temp_var}was removed")
        except ValueError | IndexError:
            print("Invalid command.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid")

print("See ya")