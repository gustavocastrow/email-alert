import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
  msg = EmailMessage()
  msg.set_content(body)
  msg['subject'] = subject
  msg['to'] = to
  
  user = "alertatestepython@gmail.com"
  msg['from'] = user
  password = "your password here."
  #password: manage your google account > security > enable 2-step verification
  #App passwords > other > and generate a new password.

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(user, password)
  server.send_message(msg)
  server.quit()

if __name__ == '__main__':
    email_alert("Hey this is the subject", "This is the body", "gustavocastrocs@gmail.com")