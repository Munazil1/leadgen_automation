import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from reply_handler import match_replies_with_originals

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Constants
REPLY_DRAFTS_FILE = "reply_drafts.json"
CALENDLY_LINK = "https://calendly.com/munazilv1/30min"

# Load drafts if they exist
def load_existing_drafts():
    if not os.path.exists(REPLY_DRAFTS_FILE):
        return []
    try:
        with open(REPLY_DRAFTS_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

# Save a new reply draft to the file
def save_draft(entry):
    drafts = load_existing_drafts()
    if not any(d["email"] == entry["email"] and d["reply_text"] == entry["reply_text"] for d in drafts):
        drafts.append(entry)
        with open(REPLY_DRAFTS_FILE, "w") as f:
            json.dump(drafts, f, indent=2)
        print(f"💾 Saved draft for {entry['lead_name']}")
    else:
        print(f"⚠️ Draft already exists for {entry['lead_name']} - skipping.")

# Build prompt for Gemini
def build_prompt(original, reply):
    return (
        f"You are writing a professional reply to a potential lead.\n\n"
        f"📨 Original message sent:\n{original}\n\n"
        f"💬 Their reply:\n\"{reply}\"\n\n"
        f"🧠 Write a helpful and friendly reply that:\n"
        f"- Thanks them for the response\n"
        f"- Lists key digital marketing services (SEO, paid ads, content, email, social media)\n"
        f"- Invites them to book a 15–30 min meeting using this link:\n{CALENDLY_LINK}\n\n"
        f"Make it clear, professional, and conversational."
    )

# Main function to generate and store AI replies
def generate_reply_drafts():
    matches = match_replies_with_originals()
    for match in matches:
        print(f"\n🧠 Generating AI reply for {match['lead_name']}...")

        prompt = build_prompt(match["original_message"], match["reply_text"])
        try:
            response = model.generate_content(prompt)
            ai_reply = response.text.strip()

            if CALENDLY_LINK not in ai_reply:
                ai_reply += f"\n\n📅 You can book a time here: {CALENDLY_LINK}"

            print(f"\n📨 Suggested Reply to {match['email']}:\n{ai_reply}\n")

            save_draft({
                "lead_name": match["lead_name"],
                "email": match["email"],
                "original_message": match["original_message"],
                "reply_text": match["reply_text"],
                "ai_draft": ai_reply
            })

        except Exception as e:
            print(f"❌ Error from Gemini API: {e}")

if __name__ == "__main__":
    generate_reply_drafts()
