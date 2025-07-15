# send_instagram_dm.py

import os
from dotenv import load_dotenv
from instagrapi import Client

# Load credentials
load_dotenv()
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

# Target user and message
username = "samanthajain"  # ✅ Replace with actual IG username
message = (
    "Hey Samantha! 👋 I came across GrowthSpark and love what you're doing! "
    "I'm a digital marketing expert working with startups to help them grow affordably. "
    "Would love to connect and see if there's any opportunity to collaborate!"
)

# Initialize Instagram client
cl = Client()

print("🔐 Logging in to Instagram...")
try:
    cl.login(USERNAME, PASSWORD)
    print("✅ Successfully logged in!")
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit()

# Send DM
try:
    print(f"📤 Sending DM to @{username}...")
    user_id = cl.user_id_from_username(username)
    cl.direct_send(message, [user_id])
    print(f"✅ Message sent to @{username}")
except Exception as e:
    print(f"❌ Failed to send DM to @{username}: {e}")
