import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")

window = sg.Window("To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()