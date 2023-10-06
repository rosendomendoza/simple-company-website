import streamlit as st
import pandas
from send_email import send_email


st.header("Contact Us")

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Type your email address:")
    topic_select = st.selectbox('What Topic do you want to discuss?:', df["topic"])
    user_message = st.text_area("Your message:")
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: Company Website: New message from {user_email}

From: {user_email}
Topic: {topic_select}
{user_message}
"""

    if button:
        send_email(message)
        st.info("your message was sent succesfully")


