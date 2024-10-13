import datetime
import random
import time

from TaskStatus import TaskStatus


class Task:
    id: int
    name: str
    status: TaskStatus
    datetime: datetime

    async def execute(self):
        self.status = TaskStatus.PROCESSING
        print(f"task {self.name} is being executed")
        time.sleep(random.randint(1, 10))
        self.status = TaskStatus.COMPLETED
        print(f"task {self.name} completed")


    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = TaskStatus.NEW
        self.datetime = datetime.datetime.now()

    def __str__(self):
        return "Task " + self.name + " id " + str(self.id) + " status " + str(self.status)

    def __repr__(self):
        return "Task " + self.name + " id " + str(self.id) + " status " + str(self.status)

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, __value):
        return self.id == __value.id


