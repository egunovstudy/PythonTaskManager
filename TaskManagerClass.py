class TaskManagerClass(type):
    """
    Это метакласс для реализации паттерна Singleton.
    Он управляет созданием единственного экземпляра класса.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]