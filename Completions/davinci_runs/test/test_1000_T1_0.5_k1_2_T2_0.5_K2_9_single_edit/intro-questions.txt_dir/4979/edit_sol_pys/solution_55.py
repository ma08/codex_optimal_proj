
#!/usr/bin/python
import os
import time
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
user = "username"
password = "password"
 
recipients = ['email']
 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "Subject"
msg['From'] = 'email'
msg['Reply-to'] = 'email'
 
msg.preamble = "Multipart message.\n"
 
part = MIMEText("Body")
msg.attach(part)
 
part = MIMEBase('application', "octet-stream")
part.set_payload(open("file", "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="file"')
msg.attach(part)
 
server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login(user,password)
 
server.sendmail(msg['From'], emaillist , msg.as_string())
