import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv("sender")
password = os.getenv("password")

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(sender, password)
msg = EmailMessage()
msg["Subject"] = "Test subject"
msg["from"] = sender
msg["To"] = "jamesmumo443@gmail.com"
msg.set_content("hello James")
s.send_message(msg)
s.quit()
