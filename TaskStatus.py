from enum import Enum


class TaskStatus(Enum):
    NEW = 0,
    PROCESSING = 1,
    COMPLETED = 2,
    ERROR = 3
