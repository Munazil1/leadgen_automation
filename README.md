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
├── dashboard.py # Main control center (launch Streamlit tools)
├── review_dashboard.py # Approve/edit cold messages
├── reply_review_dashboard.py # Approve & send AI replies
├── ai_reply_generator.py # Uses Gemini to draft smart replies
├── mock_lead_importer.py # Loads mock leads + drafts messages
├── follow_up_scheduler.py # Sends follow-ups automatically
├── send_all_instagram_dms.py # Instagram message sender (Instagrapi)
├── linkedin_messages_exports.py # Export LinkedIn messages to CSV
├── email_sender.py # Email sending via Gmail SMTP
├── crm_logger.py # Logs activity (sent, replied, follow-up)
├── reply_handler.py # Matches inbound replies to original outreach
├── launch_phantom.py # Launches PhantomBuster Phantom
├── mock_leads.json # Mock data (name, role, email, IG, LinkedIn)
├── approved_messages.json # Approved cold messages
├── replied_messages.json # Approved AI replies
├── reply_drafts.json # AI-drafted replies awaiting review
├── crm_log.json # CRM history log
├── .env # Stores secrets and API keys
└── requirements.txt # Python dependencies


---

## 📦 Setup

### 🔐 `.env` Configuration

``env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
GOOGLE_API_KEY=your_gemini_api_key
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
PHANTOMBUSTER_API_KEY=your_phantombuster_key
PHANTOMBUSTER_PHANTOM_ID=phantom_id_here

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


