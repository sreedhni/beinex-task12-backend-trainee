# 6.Write a Python program that reads email details (sender, recipient, subject, and body) from user input and sends the email using Mailtrap
# as the SMTP server
import smtplib
from email.mime.text import MIMEText

try:
    # Prompt user for email details
    email_from = input("Enter sender's email address: ")
    email_to = input("Enter recipient's email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    # Compose the email
    message = MIMEText(body)
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = subject

    # Connect to the SMTP server (Mailtrap)
    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port =  2525  
    smtp_user = "c64add0276d603"  
    smtp_pass = "42b1d63c563642"  

    # Initiating a connection with SMTP server.
    server = smtplib.SMTP(smtp_server, smtp_port)
    # Puts the connection to the SMTP server into TLS mode.
    server.starttls()
    # Login to the mail server using username and password.
    server.login(smtp_user, smtp_pass)
    # Send the email
    server.sendmail(email_from, email_to, message.as_string())
    print("Email sent successfully!")  # Print message indicating successful email sending

except smtplib.SMTPException as e:
    print(f"SMTP Exception occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'server' in locals():
        server.quit()

