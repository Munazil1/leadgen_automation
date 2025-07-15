import json
import os
from datetime import datetime

# Define log file
CRM_LOG = "crm_logs.json"

def log_crm_event(lead_name, email, channel, status, notes=""):
    """
    Appends an activity log entry to crm_logs.json for the given lead interaction.
    """

    entry = {
        "lead_name": lead_name,
        "email": email,
        "channel": channel,  # 'email', 'linkedin', 'instagram'
        "status": status,    # e.g., 'replied', 'followed-up', 'meeting-scheduled'
        "notes": notes,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Create file if it doesn't exist
    if not os.path.exists(CRM_LOG):
        with open(CRM_LOG, "w") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(CRM_LOG, "r") as f:
            logs = json.load(f)

        logs.append(entry)

        with open(CRM_LOG, "w") as f:
            json.dump(logs, f, indent=2)

    print(f"📌 CRM log saved for {lead_name} ({status})")
