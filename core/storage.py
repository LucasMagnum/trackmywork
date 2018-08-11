import datetime
import os
from collections import namedtuple

from core import config


Task = namedtuple('Task', 'id,message,time,project,category,links,started_at,finished_at')
sep = "#|#"
show_sep = ';'

header = ('id', 'time', 'project', 'category', 'links', 'started_at', 'finished_at')


def clear():
    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

    with open(config.STORAGE_PATH_BACKUP, 'w') as backup:
        backup.writelines(lines)

    # cleaning file
    with open(config.STORAGE_PATH, 'w'):
        pass


def save(message, time, project, category, links):
    task_id = _get_next_id()
    started_at = datetime.datetime.now()

    task = Task(task_id, message, time, project, category, links, started_at, '')

    _save_task_to_file(task)
    return task


def register(message, time, project, category, links):
    task_id = _get_next_id()
    started_at, finished_at = datetime.datetime.now(), datetime.datetime.now()

    task = Task(task_id, message, time, project, category, links, started_at, finished_at)

    _save_task_to_file(task)
    return task


def remove(task_id):
    new_lines = []

    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

        for line in lines:
            id, *_ = line.split(sep)
            if not task_id == id:
                new_lines.append(line)

    if len(lines) != len(new_lines):
        with open(config.STORAGE_PATH, 'w') as storage:
            storage.writelines(new_lines)


def show_all(stdout, tail, wip, limit):
    stdout.write(show_sep.join(header))

    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

        lines = reversed(lines[-limit:]) if tail else lines[:limit]

        for line in lines:
            items = line.strip().split(sep)
            *_, finished_at = items

            if wip and finished_at:
                continue

            stdout.write(show_sep.join(items))


def show_task(stdout, task_id):
    stdout.write(show_sep.join(header))

    with open(config.STORAGE_PATH) as storage:
        for line in storage.readlines():
            items = line.strip().split(sep)
            id, *_ = items

            if id == task_id:
                stdout.write(show_sep.join(items))
                break


def _save_task_to_file(task):
    open_mode = 'a' if _storage_file_exists() else 'w'

    template = (
        f"{task.id}{sep}{task.message}"
        f"{sep}{task.time}"
        f"{sep}{task.project or ''}"
        f"{sep}{task.category or ''}"
        f"{sep}{task.links or ''}"
        f"{sep}{task.started_at}"
        f"{sep}{task.finished_at}\n"
    )

    with open(config.STORAGE_PATH, open_mode) as storage:
        storage.write(template)


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
