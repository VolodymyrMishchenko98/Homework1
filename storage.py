import json
import os
from task import Task

JSON_FILE = "tasks.json"

def load_tasks():
    """Зчитування задач з JSON файлу"""
    try:
        if not os.path.exists(JSON_FILE):
            # Якщо файл не існує, створюємо порожній
            with open(JSON_FILE, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)
            return []
        
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Конвертуємо словники в об'єкти Task
            return [Task.from_dict(task) for task in data]
    
    except FileNotFoundError:
        print("❌ Помилка: Файл tasks.json не знайдено. Створюю новий...")
        return []
    except json.JSONDecodeError:
        print("❌ Помилка: Некоректний формат JSON. Починаю заново...")
        return []
    except Exception as e:
        print(f"❌ Помилка при завантаженні: {e}")
        return []

def save_tasks(tasks):
    """Збереження задач у JSON файл"""
    try:
        if not tasks:
            print("⚠️  Список задач порожній")
            return
        
        data = [task.to_dict() for task in tasks]
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✅ Задачи збережено успішно!")
    except Exception as e:
        print(f"❌ Помилка при збереженні: {e}")
  

