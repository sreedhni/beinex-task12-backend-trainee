# 8.write a python program to handle exceptions when sending emails using Python's smtplib library.

import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPException

try:
    email_from = "sender@example.com"
    email_to = "receiver@example.com"
    subject = "Sample email"
    body = "This is a sample email to test the functionality."
    message = MIMEText(body)
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = subject

    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port =  2525
    smtp_user = "c64add0276d603"  
    smtp_pass = "42b1d63c563642" 
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(email_from, email_to, message.as_string())
    print("Email sent successfully!")  
    server.quit()

except SMTPException as e:
    print("Error: Unable to send email. SMTPException:", e)
except Exception as e:
    print("Error:", e)
