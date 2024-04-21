import smtplib
import emails_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to, subject, message):
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = subject
    multipart_message["from"] = f"Scomperleur <{emails_config.config_email}>"
    multipart_message["to"] = to
    # multipart_message.attach(MIMEText(message, "plain"))
    multipart_message.attach(MIMEText(message, "html"))


    server_mail = smtplib.SMTP(emails_config.config_server, emails_config.config_server_port)
    server_mail.starttls()
    server_mail.login(emails_config.config_email, emails_config.config_password)
    server_mail.sendmail(emails_config.config_email, to, multipart_message.as_string())
    server_mail.quit()

message = """
Bonjour
<br/>
<br/>
Comment allez-vous ?
<br/>
<br/>
<strong>Merci</strong>.
"""
send_email("test-1-scomp-22042024@yopmail.com", "Prise de contact", message)
