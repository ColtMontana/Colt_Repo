import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.sent_content(body)
    msg['subject'] = subject
    msg['to'] = to


    user = "coltcodemail@gmail.com"
    password = "bhbcisqohiogntxm"

    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

    if __name__ == '__main__':
        email_alert("Hey", "Hello world", "coltonmac90@gmail.com")