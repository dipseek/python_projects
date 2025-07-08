import streamlit as st
import os

st.set_page_config(page_title="Automation Dashboard", page_icon="⚙")
st.title("🧠 System Automation Panel")

st.markdown("""
### What would you like to do?
""")

option = st.selectbox("Choose an action:", [
    "Open or Create File in Notepad",
    "Open Jupyter Notebook",
    "Open or Create File in VS Code",
    "Create Folder at Custom Location",
    "Open Paint",
    "Open Website in Chrome",
    "Open Virtualbox",
    "Exit"
])

if option == "Open or Create File in Notepad":
    filename = st.text_input("Enter file name to open/create in Notepad:")
    if st.button("Open Notepad"):
        os.system(f"notepad {filename}")

elif option == "Open Jupyter Notebook":
    if st.button("Launch Jupyter Notebook"):
        os.system("jupyter notebook")

elif option == "Open or Create File in VS Code":
    file = st.text_input("Enter file name to open/create in VS Code:")
    if st.button("Open VS Code"):
        os.system(f"code {file}")

elif option == "Create Folder at Custom Location":
    folder = st.text_input("Enter new folder name:")
    destination = st.text_input("Enter full destination path:")
    if st.button("Create Folder"):
        os.system(f'mkdir "{os.path.join(destination, folder)}"')
        st.success(f"Folder '{folder}' created at {destination}")

elif option == "Open Paint":
    if st.button("Open Paint"):
        os.system("mspaint")

elif option == "Open Website in Chrome":
    web = st.text_input("Enter website name (e.g., google.com):")
    if st.button("Open Website"):
        os.system(f"start chrome www.{web}")

elif option == "Open Virtualbox":
    if st.button("Open Virtualbox"):
        os.system("Oracle VirtualBox")

elif option == "Exit":
    st.warning("You chose to exit. Close the Streamlit tab if you're done.")