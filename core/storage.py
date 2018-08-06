import datetime
import os
from collections import namedtuple

from core import config


Task = namedtuple('Task', 'id,message,time,project,category,links,created_at,finished_at')
sep = "#|#"


def save(message, time, project, category, links):
    task_id = _get_next_id()
    created_at = datetime.datetime.now()

    task = Task(task_id, message, time, project, category, links, created_at, '')

    _save_task_to_file(task)
    return task


def _save_task_to_file(task):
    open_mode = 'a' if _storage_file_exists() else 'w'

    template = (
        f"{task.id}{sep}{task.message}"
        f"{sep}{task.time}"
        f"{sep}{task.project or ''}"
        f"{sep}{task.category or ''}"
        f"{sep}{task.links or ''}"
        f"{sep}{task.created_at}"
        f"{sep}{task.finished_at}\n"
    )

    with open(config.STORAGE_PATH, open_mode) as storage:
        storage.write(template)


def show_all(stdout, tail, limit):
    header = ('id', 'time', 'project', 'category', 'links', 'created_at', 'finished_at')
    show_sep = ';'

    stdout.write(show_sep.join(header))

    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

        lines = reversed(lines[-limit:]) if tail else lines[:limit]

        for line in lines:
            items = line.strip().split(sep)
            stdout.write(show_sep.join(items))


def show_task(stdout, task_id):
    header = ('id', 'time', 'project', 'category', 'links', 'created_at', 'finished_at')
    show_sep = ';'

    stdout.write(show_sep.join(header))

    with open(config.STORAGE_PATH) as storage:
        for line in storage.readlines():
            items = line.strip().split(sep)
            id, *_ = items

            if id == task_id:
                stdout.write(show_sep.join(items))
                break


def _get_next_id():
    if _storage_file_exists():
        with open(config.STORAGE_PATH, 'r+') as storage:
            return len(storage.readlines()) + 1
    return 1


def _get_last_id():
    if _storage_file_exists():
        with open(config.STORAGE_PATH, 'r+') as storage:
            return len(storage.readlines())
    return


def _storage_file_exists():
    return os.path.exists(config.STORAGE_PATH)
