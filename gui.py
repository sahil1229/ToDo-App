import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkTeal2")
clock = sg.Text('', key='clock')
layout = [[clock],
    [sg.Text("To-Do App", font=("Helvetica", 20), justification='center')],
    [sg.Text("Type in a todo:", font=("Helvetica", 12))],
    [sg.InputText(tooltip="Enter Todo", key="todo", size=(30, 1), font=("Helvetica", 12)),
     sg.Button("Add", size=(6, 1), font=("Helvetica", 12))],
    [sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10),
                font=("Helvetica", 12), bind_return_key=True)],
    [sg.Button("Edit", size=(10, 1), font=("Helvetica", 12)),
     sg.Button("Complete", size=(10, 1), font=("Helvetica", 12)),
     sg.Button("Exit", size=(10, 1), font=("Helvetica", 12))]
]

window = sg.Window("To-Do App", layout, font=("Helvetica", 12))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todos = functions.get_todos()
                if todos:
                    todo_to_edit = values['todos'][0]
                    new_todo = values['todo']
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('helvetica', 20))

        case 'Complete':
            todos = functions.get_todos()
            try:
                if todos:
                    todo_to_complete = values['todos'][0]
                    todos.remove(todo_to_complete)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('helvetica', 20))

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()
