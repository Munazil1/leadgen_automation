import json
import os

INBOX_FILE = "inbound_replies.json"
SENT_FILE = "approved_messages.json"

def load_replies():
    if not os.path.exists(INBOX_FILE):
        print("❌ No inbound replies found.")
        return []
    with open(INBOX_FILE, "r") as f:
        return json.load(f)

def load_sent_messages():
    if not os.path.exists(SENT_FILE):
        print("❌ No approved messages found.")
        return []
    with open(SENT_FILE, "r") as f:
        return json.load(f)

def match_replies_with_originals():
    replies = load_replies()
    sent_messages = load_sent_messages()
    matched = []

    for reply in replies:
        name = reply.get("name")
        reply_text = reply.get("reply_text")
        subject = reply.get("original_subject")

        # Find latest sent email with matching subject or lead_name
        original = next(
            (msg for msg in reversed(sent_messages)
             if msg.get("lead_name") == name and msg.get("channel") == "email"
             and (subject in msg.get("message", "") or subject.lower() in msg.get("message", "").lower())),
            None
        )

        if original:
            matched.append({
                "lead_name": name,
                "email": reply.get("from"),
                "reply_text": reply_text,
                "original_message": original["message"]
            })
        else:
            print(f"⚠️ No matching sent email found for {name} (subject: {subject}). Skipping.")

    return matched

if __name__ == "__main__":
    matched = match_replies_with_originals()
    for m in matched:
        print("\n🔁 Matched Reply:")
        print(f"From: {m['lead_name']} ({m['email']})")
        print(f"Original Message:\n{m['original_message']}")
        print(f"Reply Received:\n{m['reply_text']}")
