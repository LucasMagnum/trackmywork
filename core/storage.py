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


def edit(task_id, message, time, project, category, links):
    new_lines = []

    fields_edited = []

    with open(config.STORAGE_PATH) as storage:
        for line in storage.readlines():
            items = line.split(sep)
            id, *_ = items

            if task_id == id:
                _, old_message, old_time, old_project, old_category, old_links, *rest = items
                fields = (
                    ('message', old_message, message),
                    ('time', old_time, time),
                    ('project', old_project, project),
                    ('category', old_category, category),
                    ('links', old_links, links),
                )

                # Dynamically update the fields
                new_line = [id]

                for field_name, old_field, new_field in fields:
                    if new_field and old_field != new_field:
                        fields_edited.append(field_name)
                        old_field = new_field
                    new_line.append(old_field)

                new_line.extend(rest)
                line = sep.join(new_line)

            new_lines.append(line)

    with open(config.STORAGE_PATH, 'w') as storage:
        storage.writelines(new_lines)

    return task_id, fields_edited


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


def finish_last_task():
    last_id = _get_last_id()
    return finish_task(last_id)


def finish_task(task_id):
    new_lines = []

    task_finished = False

    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

        for line in lines:
            items = line.split(sep)
            id, *_, finished_at = items

            if task_id == id and not finished_at.strip():
                finished_at = datetime.datetime.now()
                items[-1] = str(finished_at) + '\n'
                line = sep.join(items)
                task_finished = True

            new_lines.append(line)

    with open(config.STORAGE_PATH, 'w') as storage:
        storage.writelines(new_lines)

    return task_id, task_finished


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
    return str(int(_get_last_id()) + 1)


def _get_last_id():
    if _storage_file_exists():
        with open(config.STORAGE_PATH, 'r+') as storage:
            readlines = storage.readlines()
            if len(readlines):
                last_line = readlines[-1]
                id, *_ = last_line.split(sep)
                return id
    return 0


def _storage_file_exists():
    return os.path.exists(config.STORAGE_PATH)
