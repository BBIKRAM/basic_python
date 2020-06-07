from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib
templates =Template(Path('templates.html').read_text())
message = MIMEMultipart()
message["from"] = "test test"
message["to"] = "tt2331938@gmail.com"
message["subject"] = "This is a test"
# message.attach(MIMEText("body"))
# body = templates.substitute({"name":"bikram"})
body = templates.substitute(name="bikram")
message.attach(MIMEText(body,"html"))
message.attach(MIMEImage(Path("image1.jpeg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("tt2331938@gmail.com","monkey don")
    smtp.send_message(message)
    print("sent.....")
    