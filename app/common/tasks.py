import celery

from app.common.exceptions import TaskTimeoutError

def sync_call(app, task_path, task_name, timeout, **kwargs):
    try:
        full_path = "{0}.{1}".format(task_path, task_name)
        task = app.send_task(full_path, **kwargs)
        return task.get(timeout=timeout)
    except celery.exceptions.TimeoutError:
        raise TaskTimeoutError(f"Task {task_name}")