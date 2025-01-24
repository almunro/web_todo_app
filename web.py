import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo.capitalize())
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Do Do App")
st.subheader("This is my To Do list")
st.write("This is my list of <b>productivity</b> do's", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a To Do to do", on_change=add_todo, key="new_todo")

# st.session_state



