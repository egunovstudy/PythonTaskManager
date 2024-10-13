import asyncio

from hw11.Task import Task
from hw11.TaskManagerClass import TaskManagerClass
from hw11.TaskStatus import TaskStatus


class TaskManager(metaclass=TaskManagerClass):
    tasks: [Task] = []

    def add_new_task(self, name: str):

        max_id = 1 if len(self.tasks) == 0 else sorted(self.tasks, key=lambda t: t.id)[-1].id

        task = Task(max_id + 1, name)

        self.tasks.append(task)
        print(f"Task {task} has been added")

    def delete_task_by_id(self, task_id: int):
        task: Task = self.find_task_by_id(task_id)
        self.tasks.remove(task)

    def find_task_by_id(self, task_id: int):
        self.__selection_sort()
        return self.__binary_search(task_id, 0, len(self.tasks) - 1)

    def show_all_tasks(self):
        print(self.tasks)

    async def execute_all_tasks(self):
        tasks = [t.execute() for t in self.tasks if t.status == TaskStatus.NEW]
        await asyncio.gather(*tasks)

    def __selection_sort(self):
        for i in range(len(self.tasks)):
            min_idx = i
            for j in range(i + 1, len(self.tasks)):
                if self.tasks[j] < self.tasks[min_idx]:
                    min_idx = j
            self.tasks[i], self.tasks[min_idx] = self.tasks[min_idx], self.tasks[i]

    def __binary_search(self, val, start_index, end_index):
        if start_index > end_index:
            return -1

        middle = (end_index + start_index) // 2
        if self.tasks[middle] is None:
            curr_idx = middle
            while curr_idx >= start_index and self.tasks[curr_idx] is None:
                curr_idx = curr_idx - 1
            if curr_idx >= start_index:
                middle = curr_idx
            else:
                curr_idx = middle
                while curr_idx <= end_index and self.tasks[curr_idx] is None:
                    curr_idx = curr_idx + 1
                if curr_idx <= end_index:
                    middle = curr_idx
                else:
                    return -1

        if self.tasks[middle].id == val:
            return middle
        elif self.tasks[middle].id < val:
            return self.__binary_search(val, middle + 1, end_index)
        else:
            return self.__binary_search(val, start_index, middle - 1)
