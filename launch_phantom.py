import os
import requests
from dotenv import load_dotenv

# Load PhantomBuster credentials
load_dotenv()

PHANTOM_ID = os.getenv("PHANTOMBUSTER_PHANTOM_ID")
API_KEY = os.getenv("PHANTOMBUSTER_API_KEY")

def launch_phantom():
    url = "https://api.phantombuster.com/api/v2/agents/launch"
    headers = {
        "X-Phantombuster-Key-1": API_KEY
    }
    params = {
        "id": PHANTOM_ID,
        "output": "first"
    }

    print("🚀 Launching PhantomBuster Phantom...")
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        print("✅ Phantom launched successfully!")
        print("📦 Status:", data.get("status", "No status returned"))
        print("🔗 Console link:", data.get("containerUrl", "N/A"))
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
        print(response.text)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    launch_phantom()
