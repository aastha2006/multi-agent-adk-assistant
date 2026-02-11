import datetime

class Session:
    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.context = []
        self.metadata = {}

    def add_context(self, role: str, content: str):
        self.context.append({"role": role, "content": content})
