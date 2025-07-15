# reply_review_dashboard.py

import streamlit as st
import json
import os
from datetime import datetime
from email_sender import send_email
from crm_logger import log_crm_event  # ✅ CRM sync

# File paths
REPLY_DRAFTS_FILE = "reply_drafts.json"
REPLY_LOG_FILE = "replied_messages.json"

# Ensure files exist
if not os.path.exists(REPLY_DRAFTS_FILE):
    st.error("❌ No reply drafts found. Please run ai_reply_generator.py first.")
    st.stop()

if not os.path.exists(REPLY_LOG_FILE):
    with open(REPLY_LOG_FILE, "w") as f:
        json.dump([], f)

# Load drafts and sent log
with open(REPLY_DRAFTS_FILE, "r") as f:
    drafts = json.load(f)

with open(REPLY_LOG_FILE, "r") as f:
    sent_log = json.load(f)

# Exclude already replied
sent_emails = [entry["email"] for entry in sent_log]
pending_drafts = [d for d in drafts if d["email"] not in sent_emails]

# Streamlit UI setup
st.set_page_config(page_title="Reply Review", layout="wide")
st.title("📬 AI-Generated Replies to Inbound Queries")

if not pending_drafts:
    st.info("✅ All replies have been reviewed and sent.")
    st.stop()

# Iterate through replies
for i, draft in enumerate(pending_drafts):
    key_base = f"{draft['email']}_{i}"

    with st.expander(f"💬 Reply from {draft['lead_name']} ({draft['email']})", expanded=True):
        st.markdown(f"**📝 Original Message Sent:**\n\n{draft['original_message']}")
        st.markdown(f"**💬 Their Reply:**\n\n> {draft['reply_text']}")

        edited = st.text_area(
            "✏️ Edit AI Reply",
            value=draft["ai_draft"],
            height=300,
            key=f"text_{key_base}"
        )

        col1, col2 = st.columns([1, 1])

        # ✅ Approve & Send
        with col1:
            if st.button(f"✅ Approve & Send", key=f"send_{key_base}"):
                subject = f"Re: {draft['original_message'].splitlines()[0].replace('**', '').strip()}"
                success = send_email(to=draft["email"], subject=subject, body=edited)

                if success:
                    sent_log.append({
                        "lead_name": draft["lead_name"],
                        "email": draft["email"],
                        "reply_text": edited,
                        "timestamp": datetime.utcnow().isoformat()
                    })
                    with open(REPLY_LOG_FILE, "w") as f:
                        json.dump(sent_log, f, indent=2)

                    # ✅ CRM Sync
                    log_crm_event(
                        lead_name=draft["lead_name"],
                        email=draft["email"],
                        channel="email",
                        status="replied",
                        notes="AI-generated reply approved & sent"
                    )

                    st.success(f"✅ Reply sent to {draft['email']}")
                else:
                    st.error(f"❌ Failed to send email to {draft['email']}")

        # ❌ Skip
        with col2:
            if st.button(f"❌ Skip", key=f"skip_{key_base}"):
                st.warning(f"⏭️ Skipped reply to {draft['email']}")
