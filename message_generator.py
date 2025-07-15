# message_generator.py
def generate_message(lead, channel):
    first_name = lead.name.split()[0]

    if channel == "email":
        return f"""**Subject: Affordable Growth for {lead.company}?**

**Body:**

Hi {first_name},

I'm [Your Name], a digital marketing expert specializing in helping startups like {lead.company} achieve significant growth without breaking the bank.

I've noticed {lead.company}'s recent activities and believe my strategies in SEO, content marketing, and paid social can help you scale faster.

Would you be open to a quick 15-minute call to explore opportunities?

Best regards,  
[Your Name]  
[Your Website/LinkedIn Profile]"""

    elif channel == "linkedin":
        return (
            f"Hi {first_name}, I'm a digital marketing expert focused on helping startups like "
            f"{lead.company} achieve significant growth without breaking the bank. "
            f"Your work at {lead.company} is impressive, and I'd love to connect and see if there are "
            f"any opportunities for collaboration. Would you be open to a quick chat sometime next week?"
        )

    elif channel == "instagram":
        return (
            f"Hey {first_name}! 👋 Saw your awesome work at {lead.company} and wanted to reach out. "
            f"As a digital marketing expert who helps startups like yours achieve big growth without "
            f"breaking the bank, I’d love to connect. Would you be open to a quick chat sometime next week?"
        )

    else:
        return f"Hi {first_name}, I’d love to connect regarding {lead.company}!"

