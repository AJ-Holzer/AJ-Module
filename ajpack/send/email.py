from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
import smtplib
import os

def send_email(
        sender_email: str,
        sender_pwd: str,
        receiver_email: str,
        body: str,
        subject: str,
        mode: str = "plain",
        attachment_paths: list[str] = [],
        timeout: float = 10,
        smtpServerDomain: str = "smtp.gmail.com",
        port: int = 587
) -> None:
    """
    Sends an email to a receiver via gmail.
    
    :param sender_email: The host email.
    :param sender_pwd: The password of the host email.
    :param receiver_email: The email of the receiver.
    :param body: The content of the email.
    :param subject: The subject of the email.
    :param mode: The mode of the text in the body. (e.g. html, plain, ...)
    :param attachment_path: The path to the file to be attached.
    :param timeout: The timeout of the email sending process in seconds.
    """
    try:
        # Set up the MIME
        message: MIMEMultipart = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        
        # Attach the body with the msg instance
        message.attach(MIMEText(body, mode))
        
        # Attach the file if provided
        for attachment_path in attachment_paths:
            if attachment_path:
                filename = os.path.basename(attachment_path)
                with open(attachment_path, 'rb') as f:
                    attachment = MIMEApplication(f.read(), Name=filename)
                attachment['Content-Disposition'] = f'attachment; filename="{filename}"'
                message.attach(attachment)
        
        # Create SMTP session for sending the mail
        server: smtplib.SMTP = smtplib.SMTP(smtpServerDomain, port, timeout=timeout)
        server.starttls() # Enable security
        
        # Login with your email and password
        server.login(sender_email, sender_pwd)
        
        # Convert the message to a string and send it
        text: str = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        # Terminate the SMTP session and close the connection
        server.quit()
    except smtplib.SMTPException as e:
        raise Exception(f"SMTP error: {e}")
    except OSError as e:
        raise Exception(f"OS error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
