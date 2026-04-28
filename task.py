class Task:
    """Клас для представлення задачи у Task Manager"""
    
    def __init__(self, id, title, description, status="todo", priority="medium"):  
        """
        Ініціалізація задачи
        
        Args:
            id (int): Унікальний ідентифікатор
            title (str): Назва задачи
            description (str): Опис задачи
            status (str): Статус - "todo" або "done"
            priority (str): Пріоритет - "low", "medium" або "high"
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
    
    def to_dict(self):
        """Конвертація задачи в словник для JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }
    
    @staticmethod
    def from_dict(data):
        """Створення об'єкта Task зі словника"""
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=data.get("status", "todo"),
            priority=data.get("priority", "medium")
        )
    
    def __str__(self):
        """Рядкове представлення задачи"""
        return f"[{self.id}] {self.title} - {self.status}"