class Lead:
    def __init__(self, name, role, email, company, source="manual", linkedin=None, instagram=None):
        self.name = name
        self.role = role
        self.email = email
        self.company = company
        self.source = source
        self.linkedin = linkedin
        self.instagram = instagram

    def __repr__(self):
        return f"<Lead {self.name} - {self.role} @ {self.company}>"

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "email": self.email,
            "company": self.company,
            "source": self.source,
            "linkedin": self.linkedin,
            "instagram": self.instagram
        }
