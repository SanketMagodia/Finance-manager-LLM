import streamlit as st
from streamlit_mic_recorder import mic_recorder, speech_to_text
import api
import json
import pandas as pd
import RegressorPlot

# st.session_state.token = "65e7df260d8458d99a57371a"
def dataFetch():
    data = json.loads(api.reqData(st.session_state.token) )   
    return pd.DataFrame(data)

    

def record_page():
    c1, c2 = st.columns(2)
    with c1:
        st.write("Tell us about your expenses :")
    with c2:
        text = speech_to_text(language='en', use_container_width=True, just_once=True, key='STT')
        
    if text:
        st.text(text)
        response = api.speach(st.session_state.token, text)
        st.success(response['response'])

    df = pd.DataFrame(dataFetch())
    df = df[::-1][["item", "price", "dates"]]
    rows_to_display = 3


    with st.expander("Expand Table"):
        st.table(df[:rows_to_display])
        show_more = st.checkbox("Show more rows")
        if show_more:
            rows_to_display = len(df)
            st.table(df)
    df['dates'] = pd.to_datetime(df['dates'])
    st.sidebar.header('Filter Options')

    # Filter by time period
    selected_period = st.sidebar.selectbox('Select time period:', ['One Month', 'Two Months', 'Lifetime'])
    c1, c2,  = st.columns(2)
    with c1:
        st.write("Record and we'll figure out")
        # Create a text input box
        user_input = st.sidebar.text_area(" Ask your personal Finance Questions:")
    with c2:
        # Create a button to submit the message
        submit_button = st.sidebar.button("Submit")
    if submit_button and user_input:
        response = api.AskLLM(st.session_state.token, user_input)
        paragraphs = str(response['response']).split('\n')
        for paragraph in paragraphs:
            st.sidebar.write(paragraph)    
    # Filter DataFrame based on selected time period
    if selected_period == 'One Month':
        filtered_df = df[df['dates'] >= df['dates'].max() - pd.DateOffset(months=1)]
    elif selected_period == 'Two Months':
        filtered_df = df[df['dates'] >= df['dates'].max() - pd.DateOffset(months=2)]
    else:
        filtered_df = df

    aggregated_df = filtered_df.groupby('dates').sum().reset_index()
    RegressorPlot.regressor(aggregated_df)