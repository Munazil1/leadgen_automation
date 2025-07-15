# send_test_to_leads.py

import json
import re
from email_sender import send_email

LEADS_FILE = "mock_leads.json"
EMAIL_LOG_FILE = "test_email_log.json"

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def load_leads():
    with open(LEADS_FILE, "r") as f:
        return json.load(f)

def log_result(result):
    try:
        with open(EMAIL_LOG_FILE, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(result)

    with open(EMAIL_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def main():
    leads = load_leads()

    for lead in leads:
        name = lead.get("name")
        company = lead.get("company")
        email = lead.get("email") or f"{name.split()[0].lower()}@gmail.com"

        if not name or not company:
            print(f"⚠️ Skipping incomplete lead: {lead}")
            continue

        if not is_valid_email(email):
            print(f"❌ Invalid email: {email}")
            continue

        subject = f"Hi {name}, just testing our outreach system"
        body = f"""Hi {name},

This is a test email from our automated AI outreach system.

I came across your work at {company} and just wanted to confirm delivery is working correctly.

Thanks!

— Your AI Bot
"""

        print(f"📤 Sending test to {email}...")
        success = send_email(email, subject, body)

        log_result({
            "name": name,
            "email": email,
            "status": "success" if success else "failed"
        })

if __name__ == "__main__":
    main()
