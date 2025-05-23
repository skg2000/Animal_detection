import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    if not hasattr(email_alert, "has_run"):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "youremail@gmail.com"
        msg['from'] = user
        password = "password(16)"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
        email_alert.has_run = True


