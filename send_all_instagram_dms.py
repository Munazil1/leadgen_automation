# send_all_instagram_dms.py

import os
import json
from dotenv import load_dotenv
from instagrapi import Client

# Load environment variables
load_dotenv()
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

# File paths
LEADS_FILE = "mock_leads.json"
MESSAGES_FILE = "approved_messages.json"

# Load data
with open(LEADS_FILE) as f:
    leads = json.load(f)

with open(MESSAGES_FILE) as f:
    messages = json.load(f)

# Build mapping from lead name to Instagram handle
lead_map = {lead["name"]: lead.get("instagram") for lead in leads}

# Initialize Instagram client
cl = Client()

print("🔐 Logging into Instagram...")
try:
    cl.login(USERNAME, PASSWORD)
    print("✅ Logged in successfully!\n")
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit()

# Filter messages for Instagram channel
insta_messages = [
    m for m in messages
    if m["channel"] == "instagram" and m["status"] == "sent"
]

# Send DMs
for entry in insta_messages:
    name = entry["lead_name"]
    handle = lead_map.get(name)
    message = entry["message"]

    if not handle:
        print(f"⚠️ No Instagram handle found for {name}. Skipping.\n")
        continue

    # Clean up handle if it's a URL
    username = handle.replace("https://instagram.com/", "").strip("/")

    try:
        print(f"📤 Sending DM to @{username}...")
        user_id = cl.user_id_from_username(username)
        cl.direct_send(message, [user_id])
        print(f"✅ Message sent to @{username}\n")
    except Exception as e:
        print(f"❌ Failed to send to @{username}: {e}\n")
