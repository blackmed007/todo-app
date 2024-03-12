import streamlit as st
import functions

todos_list = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos_list.append(todo.strip().title() + '\n')
    functions.write_todos(lst_name=todos_list, action='w')


st.title("Welcome to To Do App")

for index, todo in enumerate(todos_list):
    check_box=st.checkbox(todo, key=todo)
    if check_box:
        todos_list.remove(todo)
        functions.write_todos(lst_name=todos_list, action='w')
        del st.session_state["new_todo"]
        st.experimental_rerun()


st.text_input(label='', placeholder='Add a New ToDo ...  ',
              on_change=add_todo, key='new_todo')

