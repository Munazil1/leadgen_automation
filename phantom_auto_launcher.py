import os
import requests
from dotenv import load_dotenv

load_dotenv()

PHANTOM_ID = os.getenv("PHANTOMBUSTER_PHANTOM_ID")
API_KEY = os.getenv("PHANTOMBUSTER_API_KEY")

HEADERS = {
    "X-Phantombuster-Key-1": API_KEY,
    "Content-Type": "application/json"
}

def launch_phantom():
    print("🚀 Launching Phantom...")

    url = "https://api.phantombuster.com/api/v2/agents/launch"
    params = {
        "id": PHANTOM_ID,
        "output": "first"
    }

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        print("✅ Phantom launched!")
        print("📦 Run ID:", response.json().get("containerId"))
    else:
        print(f"❌ Error launching Phantom: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    launch_phantom()
