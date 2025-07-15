# email_sender.py

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = os.getenv("EMAIL_ADDRESS")
EMAIL_PASS = os.getenv("EMAIL_PASSWORD")


def send_email(to, subject, body, html=None):
    if not EMAIL_USER or not EMAIL_PASS:
        print("❌ Missing EMAIL credentials in environment variables.")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to

    # Plain text fallback + optional HTML
    part1 = MIMEText(body, "plain")
    msg.attach(part1)

    if html:
        part2 = MIMEText(html, "html")
        msg.attach(part2)

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
            print(f"✅ Email sent to {to}")
            return True
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Check your EMAIL_USER and EMAIL_PASS.")
    except Exception as e:
        print(f"❌ Failed to send email to {to}: {e}")

    return False
