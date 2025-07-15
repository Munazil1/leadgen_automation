# mock_lead_importer.py

import json
from lead import Lead
from message_generator import generate_message
from datetime import datetime
import os

# Config
CHANNELS = ["linkedin", "email", "instagram"]
MOCK_FILE = "mock_leads.json"
OUTPUT_JSON = "approved_messages.json"

# Ensure output file exists
if not os.path.exists(OUTPUT_JSON):
    with open(OUTPUT_JSON, "w") as f:
        json.dump([], f)

def save_message(lead_name, channel, message, email=None):
    entry = {
        "lead_name": lead_name,
        "channel": channel,
        "message": message,
        "status": "sent",
        "timestamp": datetime.utcnow().isoformat()
    }

    if channel == "email" and email:
        entry["email"] = email

    with open(OUTPUT_JSON, "r") as f:
        data = json.load(f)

    data.append(entry)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Saved message for {lead_name} ({channel})")

def import_mock_leads():
    with open(MOCK_FILE) as f:
        leads_data = json.load(f)

    for item in leads_data:
        name = item["name"]
        first_name = name.split()[0].lower()
        email = f"{first_name}@gmail.com"  # 💡 consistent testable format

        lead = Lead(
            name=name,
            role=item["role"],
            email=email,
            company=item["company"],
            source="mock",
            linkedin=item.get("linkedin"),
            instagram=item.get("instagram")
        )

        print(f"\n👤 Generating messages for {lead.name}...")

        for channel in CHANNELS:
            try:
                msg = generate_message(lead, channel)
                print(f"\n📨 {channel.capitalize()} Message:\n{msg}\n")
                save_message(lead.name, channel, msg, email=email)
            except Exception as e:
                print(f"❌ Failed to generate {channel} message for {lead.name}: {e}")

if __name__ == "__main__":
    import_mock_leads()
