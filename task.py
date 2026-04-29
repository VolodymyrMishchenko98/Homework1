class Task:
    
    def __init__(self, id, title, description, status="todo", priority="medium"):  
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=data.get("status", "todo"),
            priority=data.get("priority", "medium")
        )
    
    def __str__(self):
        return f"[{self.id}] {self.title} - {self.status}"
