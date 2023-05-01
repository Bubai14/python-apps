import streamlit as st
import notification as notify

st.header("Contact Us")

with st.form(key="email-forms"):
    user_email = st.text_input("Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")
    button = st.form_submit_button("Send")
    if button:
        notify.send_mail(user_email, subject, message)