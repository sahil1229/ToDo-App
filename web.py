import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    new_todo = st.session_state["new_todo"]+"\n"
    todos.append(new_todo)
    functions.write_todos(todos)

def special_message():
    message= st.session_state["special_message"]
    functions.write_todos(message, "message.txt")

st.title("ToDo App")
st.write("Dont add too many tasks")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a task Khushi Sethi",
              on_change=add_todo, key='new_todo')
st.text_input(label="",placeholder="Any special message for owner",
              on_change=special_message, key='special_message')