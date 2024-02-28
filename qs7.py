# .write a python program to send an email with multiple recipients using the smtplib library.

import smtplib
from email.mime.text import MIMEText

# Compose the email
email_from = "sender@example.com"
email_to = ["receiver1@example.com", "receiver2@example.com"]  
subject = "Sample email"
body = "This is a sample email to test the functionality."

# Connect to the SMTP server
smtp_server = "sandbox.smtp.mailtrap.io"
smtp_port = 2525  
smtp_user = "c64add0276d603"  
smtp_pass = "42b1d63c563642"  
try:
    # Initiating a connection with SMTP server.
    server = smtplib.SMTP(smtp_server, smtp_port)
    # Puts the connection to the SMTP server into TLS mode.
    server.starttls()
    # Login to the mail server using username and password.
    server.login(smtp_user, smtp_pass)

    for recipient in email_to:
        # Compose the email
        message = MIMEText(body)
        message['From'] = email_from
        message['To'] = recipient
        message['Subject'] = subject
        # Send the email
        server.sendmail(email_from, recipient, message.as_string())
        print(f"Email sent successfully to {recipient}!")

except smtplib.SMTPException as e:
    print(f"SMTP Exception occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if 'server' in locals():
        server.quit()