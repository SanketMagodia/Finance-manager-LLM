import streamlit as st
import api
import json 
import register
import record

def authenticate(email, password):
    id = api.login(email, password)
    
    if id['id'] == "not found":
        return False
    else:
        st.session_state.token = id['id']
        return True

def login_page():
    placeholder = st.empty()
    with placeholder.form("login"):
        st.title("Login Page")
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        reg = st.form_submit_button("Register")
    
    if submit and authenticate(email, password):
        st.success("Login successful!")
        # Set a session state variable to indicate that the user is logged in
        st.session_state.logged_in = True
        placeholder.empty()
        record.record_page()
    elif submit and not authenticate(email, password):
        st.error("Invalid username or password")
    if reg:
        placeholder.empty()
        register.register_page()

