import streamlit as st
import requests

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=648da32d2290e0e0341d7352&org=ffb8ede1-0fb3-43ba-a1b0-2d3a169404f2"
headers = {
    'Authorization':'Bearer 99e190fa-bc22-4a63-9b92-9278f3cae91e',
    'Content-Type': 'application/json'
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def main():
    st.set_page_config(page_title="REQUIREMENTS GENERATOR", page_icon=":tada:", layout="wide")
    st.subheader("ENGINEER YOUR REQUIREMENTS HERE")
    st.write("Please Enter your requirement Below")
    user_question = st.text_input("Follow this documentation")
    if(user_question):
        with st.spinner("Processing"):
            print("processing")
            payload={
                "in-0":user_question
            }
            response1 = query(payload)
            st.write(response1['out-2'])

if __name__ == '__main__':
    main()
