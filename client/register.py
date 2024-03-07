import streamlit as st
import api
import record

# from authentication import register_user
def authenticate(email, username, password):
    id = api.register(email, username, password)
    try:
        id['id']
        if id['id'] == "not found":
            return False
        else:
            st.session_state.token = id['id']
            return True
    except:
        return False
    
    
def register_page():
    placeholderR = st.empty()
    with placeholderR.form('Register'):
        st.title("User Registration")
        st.markdown("#### Enter your credentials")
    # Input fields for username, password, and email
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Register")
        
    # Button to submit registration form
    if submit and authenticate(email, username, password):
        print("lodaaaaaa")
        st.success("Success!!")
        placeholderR.empty()
        record.record_page()
    elif submit and not authenticate(email,username, password):
        st.error("Invalid username, email or password")