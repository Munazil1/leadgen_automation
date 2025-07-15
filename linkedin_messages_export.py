# linkedin_messages_exports.py

import json
import csv

APPROVED_JSON = "approved_messages.json"
OUTPUT_CSV = "phantombuster_linkedin_messages.csv"

# ✅ Static name-to-LinkedIn mapping (could be extended or loaded from mock_leads.json)
def get_linkedin_url(name):
    mapping = {
        "Raj Mehta": "https://www.linkedin.com/in/rajmehta",
        "Ananya Rao": "https://www.linkedin.com/in/ananyarao",
        "Samantha Jain": "https://www.linkedin.com/in/samanthajain",
        "Munazilv1": "https://www.linkedin.com/in/munazilv1"
    }
    return mapping.get(name)

def export_linkedin_messages():
    try:
        with open(APPROVED_JSON, "r") as f:
            messages = json.load(f)
    except Exception as e:
        print(f"❌ Error reading approved messages: {e}")
        return

    linkedin_rows = []
    for entry in messages:
        if entry["channel"] != "linkedin":
            continue

        profile_url = get_linkedin_url(entry["lead_name"])
        if not profile_url:
            print(f"⚠️ No LinkedIn URL for {entry['lead_name']}. Skipping.")
            continue

        linkedin_rows.append({
            "profileUrl": profile_url,
            "message": entry["message"]
        })

    if not linkedin_rows:
        print("⚠️ No LinkedIn messages found to export.")
        return

    try:
        with open(OUTPUT_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["profileUrl", "message"])
            writer.writeheader()
            writer.writerows(linkedin_rows)
        print(f"✅ Exported {len(linkedin_rows)} LinkedIn messages to `{OUTPUT_CSV}`")
    except Exception as e:
        print(f"❌ Failed to write CSV: {e}")

if __name__ == "__main__":
    export_linkedin_messages()
