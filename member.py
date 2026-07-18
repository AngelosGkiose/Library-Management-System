class Member:
    def __init__(self, name,email,member_id=None):
        self.name = name
        self.email = email
        self.member_id = member_id

    def __str__(self):
        return f"{self.name} | {self.email}"



