# dashboard.py

import streamlit as st
import subprocess

st.set_page_config(page_title="LeadGen Control Center", layout="wide")
st.title("🧠 LeadGen Automation Console")

st.markdown("""
Welcome to the **LeadGen Automation Dashboard**. Use the buttons below to trigger each stage of your automated outreach pipeline.

---  
""")

# Fetch and draft leads
if st.button("📥 Run Lead Fetcher & Draft Generator"):
    subprocess.run(["python3", "mock_lead_importer.py"])
    st.success("✅ Leads fetched and message drafts created!")

# Manual message review
if st.button("📝 Launch Message Review Dashboard"):
    st.info("Launching in new tab...")
    subprocess.run(["streamlit", "run", "review_dashboard.py"])

# Follow-up messages
if st.button("🔁 Run Follow-Up Scheduler"):
    subprocess.run(["python3", "follow_up_scheduler.py"])
    st.success("✅ Follow-up processing complete!")

# Process inbound replies
if st.button("📨 Process Inbound Replies + AI Drafts"):
    subprocess.run(["python3", "reply_handler.py"])
    subprocess.run(["python3", "ai_reply_generator.py"])
    st.success("✅ Inbound replies matched and AI drafts generated!")

# Human approval of AI-generated replies
if st.button("✅ Launch Reply Review Dashboard"):
    st.info("Launching in new tab...")
    subprocess.run(["streamlit", "run", "reply_review_dashboard.py"])

# Send LinkedIn DMs via PhantomBuster
if st.button("📤 Export LinkedIn DMs + Launch Phantom"):
    subprocess.run(["python3", "linkedin_messages_exports.py"])
    subprocess.run(["python3", "launch_phantom.py"])
    st.success("✅ LinkedIn DMs exported and Phantom launched!")

# Send all Instagram DMs
if st.button("📸 Send Instagram DMs"):
    subprocess.run(["python3", "send_all_instagram_dms.py"])
    st.success("✅ Instagram DMs sent!")
