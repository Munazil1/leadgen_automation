# review_dashboard.py

import streamlit as st
import json
import os
import csv
from datetime import datetime
from message_generator import generate_message
from lead import Lead

# --- File Paths ---
MOCK_FILE = "mock_leads.json"
APPROVED_FILE = "approved_messages.json"
PHANTOM_CSV = "phantombuster_linkedin_messages.csv"

# --- UI Setup ---
st.set_page_config(page_title="Lead Review", layout="wide")
st.title("📝 AI Outreach Message Review Dashboard")

CHANNELS = ["email", "linkedin", "instagram"]

# --- Load Leads ---
if not os.path.exists(MOCK_FILE):
    st.error("❌ mock_leads.json not found.")
    st.stop()

with open(MOCK_FILE) as f:
    raw_leads = json.load(f)

leads = [
    Lead(
        name=item["name"],
        role=item["role"],
        email=f"{item['name'].split()[0].lower()}@gmail.com",
        company=item["company"],
        source="mock",
        linkedin=item.get("linkedin"),
        instagram=item.get("instagram")
    )
    for item in raw_leads
]

# --- Load Approved Messages ---
if not os.path.exists(APPROVED_FILE):
    with open(APPROVED_FILE, "w") as f:
        json.dump([], f)

with open(APPROVED_FILE) as f:
    approved_messages = json.load(f)

# --- Helper Functions ---
def save_message(lead_name, channel, message, email=None):
    entry = {
        "lead_name": lead_name,
        "channel": channel,
        "message": message,
        "status": "sent",
        "timestamp": datetime.utcnow().isoformat()
    }
    if channel == "email":
        entry["email"] = email

    approved_messages.append(entry)

    with open(APPROVED_FILE, "w") as f:
        json.dump(approved_messages, f, indent=2)

    st.success(f"✅ Message for {channel} saved and marked as sent.")

def export_linkedin_csv():
    linkedin_rows = []
    for msg in approved_messages:
        if msg["channel"] == "linkedin":
            handle = next((l.get("linkedin") for l in raw_leads if l["name"] == msg["lead_name"]), None)
            if handle:
                linkedin_rows.append({"profileUrl": handle, "message": msg["message"]})

    with open(PHANTOM_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["profileUrl", "message"])
        writer.writeheader()
        writer.writerows(linkedin_rows)

    return len(linkedin_rows)

# --- UI: Lead Selector ---
lead_names = [l.name for l in leads]
selected = st.selectbox("🔍 Select Lead to Review", lead_names)
lead = next(l for l in leads if l.name == selected)

# --- UI: Show Info ---
st.markdown(f"### 👤 {lead.name} — {lead.role} at {lead.company}")
st.write(f"📧 {lead.email}  |  🔗 [LinkedIn]({lead.linkedin})  |  📸 [Instagram]({lead.instagram})")

# --- UI: Channel Review ---
for channel in CHANNELS:
    st.subheader(f"✉️ {channel.capitalize()} Message")

    existing = next((m for m in approved_messages if m["lead_name"] == lead.name and m["channel"] == channel), None)
    status = existing["status"] if existing else "not_sent"
    label = {"sent": "🟡 Sent", "followed-up": "🟢 Followed-up"}.get(status, "⚪️ Not Sent")

    st.markdown(f"**Status:** {label}")

    ai_msg = generate_message(lead, channel)
    edited = st.text_area(
        f"✏️ Edit {channel} Message",
        value=ai_msg,
        height=150,
        key=f"{channel}_{lead.name}"
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button(f"✅ Approve & Save – {channel}", key=f"save_{channel}_{lead.name}"):
            save_message(lead.name, channel, edited, email=lead.email)

    with col2:
        if st.button(f"❌ Reject – {channel}", key=f"reject_{channel}_{lead.name}"):
            st.warning(f"{channel.capitalize()} message rejected.")

# --- Export to LinkedIn CSV ---
st.markdown("---")
st.subheader("📤 Export Approved LinkedIn Messages to PhantomBuster")

if st.button("📎 Export to CSV"):
    count = export_linkedin_csv()
    st.success(f"✅ Exported {count} messages to `{PHANTOM_CSV}`")
