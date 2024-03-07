import streamlit as st
from streamlit_mic_recorder import mic_recorder, speech_to_text
import api
import json
import pandas as pd
st.session_state.token = "65e7df260d8458d99a57371a"
def dataFetch():
    data = json.loads(api.reqData(st.session_state.token) )   
    return pd.DataFrame(data)

    

def record_page():
    state = st.session_state

    
        

    c1, c2 = st.columns(2)
    with c1:
        st.write("Convert speech to text:")
    with c2:
        text = speech_to_text(language='en', use_container_width=True, just_once=True, key='STT')
        
    if text:
        st.text(text)
        response = api.speach(st.session_state.token, text)
        st.success(response['response'])

    
        

    # st.write("Record your voice, and play the recorded audio:")
    # audio = mic_recorder(start_prompt="⏺️", stop_prompt="⏹️", key='recorder')

    # if audio:
    #     st.audio(audio['bytes'])
    import pandas as pd

# Sample data
    
    # Create a DataFrame
    df = pd.DataFrame(dataFetch())
    df = df[::-1]
    # Display the table
    # st.table(df)
    rows_to_display = 5

# Display the table in an expander
    with st.expander("Expand Table"):
    # Limit the table to a certain number of rows
        st.table(df[:rows_to_display])

        # Checkbox to show more rows
        show_more = st.checkbox("Show more rows")
        if show_more:
            # Increase the number of rows to display
            rows_to_display = len(df)
            # Display the updated table
            st.table(df)
record_page()
