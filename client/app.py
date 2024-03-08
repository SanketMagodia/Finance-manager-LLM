import streamlit as st
import api
import record, login, register

def main():
    st.write("# Smart Manager")
    # st.sidebar.success("Select a demo above.")
    
    if "token" not in st.session_state:
       
        st.session_state.token = None
    if st.session_state.token is None:
        # User is not logged in, show the login page
        login.login_page()

    else:
        # User is logged in, show the record page
        record.record_page()
if __name__ == "__main__":
    main()
