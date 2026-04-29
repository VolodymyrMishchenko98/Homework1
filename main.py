import datetime
from storage import load_tasks, save_tasks
from task import Task

def print_tasks(tasks):
    if not tasks:
        print('📭 Задач немає. Список порожній!\n')
        return
    
    def sort_key(task):
        status_priority = 0 if task.status == "todo" else 1  
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return (status_priority, priority_order.get(task.priority, 1), task.id)
    
    sorted_tasks = sorted(tasks, key=sort_key)
    
    print('\n📋 ВАШІ ЗАДАЧИ (невиконані спочатку, потім за пріоритетом):')
    print('='*60)
    for task in sorted_tasks:
        status_emoji = "✅" if task.status == "done" else "⏳"
        priority_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(task.priority, "🟡")
        print(f'{status_emoji} [{task.id}] {task.title} {priority_emoji}')
        print(f'   📝 Опис: {task.description}')
        print(f'   Статус: {task.status} | Пріоритет: {priority_emoji} {task.priority}')
        print("-" * 60)
    print()

def add_task(tasks):
        
    print("\n ----ДОДАВАННЯ НОВОЇ ЗАДАЧІ----")
    try:
        title = input("Назва задачі: ").strip()
        if not title:
            print(" Назва не може бути порожною!")
            return
            
        description = input("Опис задачі: ").strip()
        if not description:
            print(" Опис не може бути порожним!")
            return
        
        print("Виберіть пріоритет:")
        print("1. 🟢 low (низький)")
        print("2. 🟡 medium (середній)")
        print("3. 🔴 high (високий)")
        priority_choice = input("Пріоритет (1-3, за замовчуванням 2): ").strip()
        
        priority_map = {"1": "low", "2": "medium", "3": "high"}
        priority = priority_map.get(priority_choice, "medium")
            
        new_id = max([task.id for task in tasks], default=0) + 1
        new_task = Task(id=new_id, title=title, description=description, status="todo", priority=priority)
        tasks.append(new_task)
        save_tasks(tasks)
        print(f" Задача '{title}' успішно додана! (Пріоритет: {priority})\n")
        
    except Exception as e:
        print(f" Помилка при додаванні задачі: {e}\n")    

def delete_task(tasks):
    print("\n🗑️  ВИДАЛЕННЯ ЗАДАЧИ")
    try:
        if not tasks:
            print("❌ Немає задач для видалення!\n")
            return
            
        task_id = int(input("Введіть ID задачи для видалення: "))
        
        for i, task in enumerate(tasks):
            if task.id == task_id:
                deleted_task = tasks.pop(i)
                save_tasks(tasks)
                print(f"✅ Задача '{deleted_task.title}' видалена!\n")
                return
        
        print(f"❌ Задача з ID {task_id} не знайдена!\n")
    
    except ValueError:
        print("❌ Некоректний ID! Введіть число.\n")
    except Exception as e:
        print(f"❌ Помилка при видаленні: {e}\n")
def search_task(tasks):
    print("\n🔍 ----Пошук задачі по ID----")
    try:
        if not tasks:
            print("❌ Немає задач для пошуку!\n")
            return
            
        task_id = int(input("Введіть ID задачи для пошуку: "))
        
        for task in tasks:
            if task.id == task_id:
                print(f"\n Задача знайдена!")
                status_emoji = "✅" if task.status == "done" else "⏳"
                priority_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(task.priority, "🟡")
                print(f"{status_emoji} [{task.id}] {task.title}")
                print(f"   📝 Опис: {task.description}")
                print(f"   Пріоритет: {priority_emoji} {task.priority}")
                print(f"   Статус: {task.status}\n")
                return
        
        print(f"❌ Задача з ID {task_id} не знайдена!\n")
    
    except ValueError:
        print("❌ Некоректний ID! Введіть число.\n")
    except Exception as e:
        print(f"❌ Помилка при пошуку: {e}\n")

def mark_done(tasks):
    print("\n---Позначити задачу як виконану----")
    try:
        if not tasks:
            print("❌ Немає задач!\n")
            return
            
        task_id = int(input("Введіть ID задачи: "))
        
        for task in tasks:
            if task.id == task_id:
                if task.status == "done":
                    print(f"⚠️  Задача вже позначена як виконана!\n")
                    return
                
                task.status = "done"
                save_tasks(tasks)
                print(f"✅ Задача '{task.title}' позначена як виконана!\n")
                return
        
        print(f"❌ Задача з ID {task_id} не знайдена!\n")
    
    except ValueError:
        print("❌ Некоректний ID! Введіть число.\n")
    except Exception as e:
        print(f"❌ Помилка: {e}\n")

def edit_task(tasks):
    print("\n  ----РЕДАГУВАННЯ ЗАДАЧІ----")
    try:
        task_id = int(input("Введіть ID задачі для редагування: "))
        for task in tasks:
            if task.id == task_id:
                priority_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(task.priority, "🟡")
                print(f"\n📝 Поточні дані:")
                print(f"   Назва: {task.title}")
                print(f"   Опис: {task.description}")
                print(f"   Пріоритет: {priority_emoji} {task.priority}\n")
                
                new_title = input("Нова назва (залиште порожним, щоб залишити без змін): ").strip()
                new_description = input("Новий опис (залиште порожним, щоб залишити без змін): ").strip()
                
                print("\nЗмінити пріоритет? (залиште порожним для без змін)")
                print("1. 🟢 low (низький)")
                print("2. 🟡 medium (середній)")
                print("3. 🔴 high (високий)")
                priority_choice = input("Новий пріоритет (1-3): ").strip()
            
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if priority_choice in ["1", "2", "3"]:
                    priority_map = {"1": "low", "2": "medium", "3": "high"}
                    task.priority = priority_map[priority_choice]
                
                save_tasks(tasks)
                print(f" Задача успішно оновлена!\n")
                return
        
        print(f" Задача з ID {task_id} не знайдена!\n")
    
    except ValueError:
        print(" Некоректний ID! Введіть число.\n")
    except Exception as e:
        print(f" Помилка при редагуванні: {e}\n")

def show_menu():
    print("\n" + "="*50)
    print("КОНСОЛЬНИЙ TASK MANAGER")
    print("="*50)
    print("1️⃣  Показати всі задачи")
    print("2️⃣  Додати задачу")
    print("3️⃣  Видалити задачу")
    print("4️⃣  Позначити як виконану")
    print("5️⃣  Редагувати задачу")
    print("6️⃣  Пошук задач за ID")
    print("7️⃣  Вийти")
    print("="*50)
    choice = input("Виберіть дію (1-7): ").strip()
    return choice

def main():
    tasks = load_tasks()
    
    done_count = sum(1 for task in tasks if task.status == "done")
    todo_count = len(tasks) - done_count
    
    print(f"✅ Завантажено {len(tasks)} задач (Виконано: {done_count}, Невиконано: {todo_count})\n")
    
    while True:
        try:
            choice = show_menu()
            
            if choice == "1":
                print_tasks(tasks)
            
            elif choice == "2":
                add_task(tasks)
            
            elif choice == "3":
                print_tasks(tasks)
                delete_task(tasks)
            
            elif choice == "4":
                print_tasks(tasks)
                mark_done(tasks)
            
            elif choice == "5":
                print_tasks(tasks)
                edit_task(tasks)
            
            elif choice == "6":
                search_task(tasks)
            
            elif choice == "7":
                print("\nДо зустрічі")
                break
            
            else:
                print(" Некоректний вибір! Виберіть 1-7.\n")
            
            
        
        except KeyboardInterrupt:
            print("\n\n Програма перервана користувачем. До зустрічі!")
            break
        except Exception as e:
            print(f" Невідома помилка: {e}\n")

if __name__ == "__main__":
    main()

