# follow_up_scheduler.py

import os
import json
from datetime import datetime, timedelta
from email_sender import send_email

APPROVED_MESSAGES_FILE = "approved_messages.json"
FOLLOW_UP_DELAY_DAYS = 2

def load_messages():
    if not os.path.exists(APPROVED_MESSAGES_FILE):
        print("❌ approved_messages.json not found.")
        return []
    with open(APPROVED_MESSAGES_FILE, "r") as f:
        return json.load(f)

def save_messages(messages):
    with open(APPROVED_MESSAGES_FILE, "w") as f:
        json.dump(messages, f, indent=2)

def should_follow_up(entry):
    if entry["status"] != "sent":
        return False
    sent_time = datetime.fromisoformat(entry["timestamp"])
    return datetime.utcnow() - sent_time >= timedelta(days=FOLLOW_UP_DELAY_DAYS)

def generate_follow_up(entry):
    return (
        f"Hi {entry['lead_name']},\n\n"
        "Just wanted to follow up on my earlier message. "
        "Let me know if you'd be open to a quick chat — happy to reconnect if the timing works!\n\n"
        "Best,\n"
        "[Your Name]"
    )

def process_followups():
    messages = load_messages()
    updated = False

    for entry in messages:
        if should_follow_up(entry):
            print(f"🔁 Preparing follow-up for {entry['lead_name']} via {entry['channel']}...")

            follow_up = generate_follow_up(entry)

            if entry["channel"] == "email" and "email" in entry:
                subject = f"Following up with {entry['lead_name']}"
                sent = send_email(to=entry["email"], subject=subject, body=follow_up)
                if not sent:
                    print(f"❌ Email failed for {entry['email']}")
                    continue

            # Update record
            entry["follow_up"] = follow_up
            entry["status"] = "followed-up"
            entry["follow_up_timestamp"] = datetime.utcnow().isoformat()
            updated = True

            print(f"📨 Follow-up message sent to {entry['lead_name']}\n")

    if updated:
        save_messages(messages)
        print("✅ Follow-up status updated in approved_messages.json")
    else:
        print("⏳ No messages needed follow-up at this time.")

if __name__ == "__main__":
    process_followups()
