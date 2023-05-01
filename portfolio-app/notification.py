import smtplib
import ssl
import os

# declare the email configurations
host = "smtp.gmail.com"
port = 465
username = os.getenv("EMAIL")# "bubaibal14@gmail.com"
password = os.getenv("PASSWORD")# "yvlvxrqxtrjckquo"
context = ssl.create_default_context()


def send_mail(receiver, subject, message):
    message = f"""
    Subject:{subject} 
    {message}
    """
    with smtplib.SMTP_SSL(host, port, context=context) as email_server:
        email_server.login(username, password)
        email_server.sendmail(username, receiver, message)
        print('Message Sent!!')