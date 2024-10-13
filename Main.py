import asyncio

from hw11.Task import Task
from hw11.TaskManager import TaskManager

if __name__ == '__main__':
    taskManager: TaskManager = TaskManager()
    while True:
        print("Добро пожаловать в интерфейс управления задачами")
        print("Список команд")
        print("1 - добавить задачу")
        print("2 - найти задачу по ID")
        print("3 - удалить задачу по ID")
        print("4 - запустить все задачи")
        print("5 - вывести все задачи  ")
        num = input("Введите число:  ")
        if not num.isdigit() or int(num) > 5 or int(num) < 1:
            print("Неверный ввод")
            exit(1)
        num = int(num)
        if num == 1:
            print("Добавление задачи")
            name = input("Введите описание задачи ")
            taskManager.add_new_task(name)
            print(f"Задача {name} была добавлена")
        elif num == 2:
            print("Поиск задачи по ID")
            task_id = input("Введите ID")
            if not task_id.isdigit():
                print("Неверный ввод")
                continue
            task: Task = taskManager.find_task_by_id(int(task_id))
            print(f"По id {task_id} найдена задача {task}")
        elif num == 3:
            print("Удаление задачи по ID")
            task_id = input("Введите ID")
            if not task_id.isdigit():
                print("Неверный ввод")
                continue
            taskManager.delete_task_by_id(int(task_id))
        elif num == 4:
            print("Запуск всех задач")
            asyncio.run(taskManager.execute_all_tasks())
            print("Все задачи выполнены")
        elif num == 5:
            print("Вывод всех задач")
            taskManager.show_all_tasks()
