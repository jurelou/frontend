import traceback


class TaskError(Exception):
    def __init__(self, value=None):
        self.value = value or ""

class TaskTimeoutError(TaskError):
    def __init__(self, value):
        super(TaskError, self).__init__(value)

    def __str__(self):
        return f"Task timeout: ({self.value})"