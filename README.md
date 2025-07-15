# leadgen_automation
End-to-end AI-assisted lead generation &amp; outreach system across Email, LinkedIn, and Instagram — with human-in-the-loop review and CRM sync.

# 🧠 LeadGen Automation Platform

An AI-powered, full-stack multichannel lead generation & messaging platform that automates cold outreach, replies, follow-ups, and CRM logging — all with **human approval** at every step.

---

## 🚀 Features

- **🔍 Lead Sourcing:** Import leads from mock data or scrape from LinkedIn, Instagram, Apollo, etc.
- **📬 Multi-Channel Messaging:**
  - ✉️ Email (via Gmail SMTP)
  - 💼 LinkedIn (via PhantomBuster)
  - 📸 Instagram DMs (via [Instagrapi](https://adw0rd.github.io/instagrapi/))
- **🧠 AI-Powered Message Drafting:** Uses **Gemini Pro** (Google Generative AI) to write personalized cold messages and replies.
- **✅ Human-in-the-Loop Streamlit Dashboards:**
  - `review_dashboard.py` – Edit and approve cold messages before sending.
  - `reply_review_dashboard.py` – Review and approve AI replies to inbound messages.
- **🔁 Automated Follow-Ups:** Schedules 2–5 day follow-ups for non-responders.
- **📨 Inbound Reply Handling:**
  - Detects replies
  - AI drafts a response (with Calendly link)
  - Human reviews, edits, and sends it
- **📅 Meeting Setup via Calendly:** Automatically includes a **Calendly meeting link** in approved replies.
- **🧾 CRM Sync:** Logs activity (sent, followed-up, replied) in `crm_log.json`
- **📤 LinkedIn Automation Integration:** Exports messages to CSV for PhantomBuster messaging automation.

---

## 🛠️ Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/) – UI dashboards for approval flow
- [Gemini AI](https://ai.google.dev/) – Message generation (via Google API)
- [Instagrapi](https://github.com/adw0rd/instagrapi) – Instagram automation (login, DM)
- [PhantomBuster](https://phantombuster.com/) – LinkedIn automation
- `smtplib` – Native email sending via Gmail
- JSON – Lightweight CRM and message log

---

## 📁 Directory Structure

leadgen/

* `dashboard.py` — 🎛️ Main control center (Streamlit launcher for workflows)
* `review_dashboard.py` — ✅ Approve/edit AI-generated cold outreach messages
* `reply_review_dashboard.py` — 📬 Review & send AI replies to inbound messages
* `ai_reply_generator.py` — 🧠 Drafts replies using Google Gemini AI
* `mock_lead_importer.py` — 📥 Loads mock leads and generates message drafts
* `follow_up_scheduler.py` — 🔁 Schedules automatic follow-up messages
* `send_all_instagram_dms.py` — 📸 Sends Instagram DMs via Instagrapi
* `linkedin_messages_exports.py` — 📤 Exports LinkedIn messages to CSV (PhantomBuster format)
* `email_sender.py` — ✉️ Sends emails via SMTP (Gmail integration)
* `crm_logger.py` — 🧾 Logs CRM events (message sent, reply received, follow-up)
* `reply_handler.py` — 🔄 Matches inbound replies with original outreach messages
* `launch_phantom.py` — 🚀 Triggers PhantomBuster automation from script

**Data & Config Files:**

* `mock_leads.json` — 🧪 Sample lead data (name, company, email, IG, LinkedIn)
* `approved_messages.json` — ✅ Approved cold outreach messages
* `reply_drafts.json` — ✏️ AI-drafted replies waiting for human approval
* `replied_messages.json` — 📥 Sent replies log
* `crm_log.json` — 📊 CRM-style tracking for lead interactions
* `.env` — 🔐 API keys and secrets (Gmail, Gemini, PhantomBuster, IG login)
* `requirements.txt` — 📦 Python package dependencies
---

## 📦 Setup

### 🔐 `.env` Configuration (Secrets & API Keys)

Create a `.env` file in the project root with the following keys:

* `EMAIL_ADDRESS` – Your Gmail address (used for sending emails)
* `EMAIL_PASSWORD` – Your Gmail **App Password** (not your regular login)
* `GOOGLE_API_KEY` – Your **Gemini (Google Generative AI)** API key
* `IG_USERNAME` – Your Instagram username (used with Instagrapi)
* `IG_PASSWORD` – Your Instagram password or session string
* `PHANTOMBUSTER_API_KEY` – Your PhantomBuster API key
* `PHANTOMBUSTER_PHANTOM_ID` – Your LinkedIn Phantom's unique ID

🧪 Run Locally
💻 To get started locally with this AI LeadGen automation platform:

**1.Clone the repository**

git clone https://github.com/Munazil1/leadgen_automation.git
cd leadgen_automation

**2.Install dependencies**

pip install -r requirements.txt

**3.Configure your environment**

Configure your environment

**4.Launch the main dashboard**

streamlit run dashboard.py


