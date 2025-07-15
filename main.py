import os
from dotenv import load_dotenv
from db import create_leads_table, get_db_connection
from models import Lead

# Load env variables
load_dotenv()
API_KEY = os.getenv("APOLLO_API_KEY")


def fetch_mock_leads():
    """Return mock leads for testing."""
    print("⚠️  Apollo API not available — using mock data...")
    return [
        {
            "first_name": "Samantha",
            "last_name": "Jain",
            "title": "Founder",
            "email_status": {"email": "sam@techspark.com"},
            "organization": {"name": "TechSpark"},
            "linkedin_url": "https://linkedin.com/in/samanthajain"
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "title": "CMO",
            "email_status": {"email": "john@stripe.com"},
            "organization": {"name": "Stripe"},
            "linkedin_url": "https://linkedin.com/in/johndoe"
        },
        {
            "first_name": "Aisha",
            "last_name": "Khan",
            "title": "CEO",
            "email_status": {"email": "aisha@startuphub.in"},
            "organization": {"name": "StartupHub"},
            "linkedin_url": "https://linkedin.com/in/aishakhan"
        }
    ]


def insert_lead(lead: Lead):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO leads (name, role, email, company, source, linkedin, instagram)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        lead.name,
        lead.role,
        lead.email,
        lead.company,
        lead.source,
        lead.linkedin,
        lead.instagram
    ))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    create_leads_table()
    leads = fetch_mock_leads()
    for person in leads:
        lead = Lead(
            name=f"{person.get('first_name')} {person.get('last_name')}",
            role=person.get("title"),
            email=person.get("email_status", {}).get("email", "unknown@example.com"),
            company=person.get("organization", {}).get("name"),
            source="MockData",
            linkedin=person.get("linkedin_url"),
            instagram=None
        )
        insert_lead(lead)
        print(f"✅ Inserted lead: {lead.name}")
