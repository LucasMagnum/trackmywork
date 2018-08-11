import os
from typing import Any, List

from core import config
from core.task import Task

sep = "#|#"


def all(limit: int, reverse: bool = False, wip: bool = False) -> List[Task]:
    """
    Return all tasks.

    Args
        limit       number of tasks to return
        reverse     return tasks in reverse order
        wip         filter the work in progress tasks

    Return
        Return a list of tasks
    """
    tasks: List[Task] = []

    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

    tasks = [_convert_line_to_task(line) for line in lines]

    if wip:
        tasks = [task for task in tasks if not task.finished_at]

    if reverse:
        tasks = tasks[::-1]

    return tasks[:limit]


def get_latest() -> Task:
    """Return the last inserted task."""
    last_id = _get_last_id()
    return get_by_id(last_id)


def get_by_id(task_id: str) -> Any:
    """
    Return a task by id.

    Args
        task_id     task id to search in the storage
    """
    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

    for line in lines:
        task = _convert_line_to_task(line)

        if task_id == task.id:
            return task

    return


def save(task: Task) -> Task:
    """
    Insert or update a task into the storage.

    Args:
        task    a task to be inserted or updated

    Return
        The task after saving it into the storage
    """
    if not task.id:
        task.id = _get_next_id()
        _insert_new_task(task)
    else:
        _update_task(task)

    return task


def remove(task_id: str) -> None:
    """Remove a task from the storage file."""
    new_lines = []

    with open(config.STORAGE_PATH) as storage:
        lines = storage.readlines()

    for line in lines:
        task = _convert_line_to_task(line)

        if not task_id == task.id:
            new_lines.append(line)

    if len(lines) != len(new_lines):
        with open(config.STORAGE_PATH, 'w') as storage:
            storage.writelines(new_lines)


def clear() -> None:
    """Clear all the tasks from the storage."""
    with open(config.STORAGE_PATH, 'w'):
        pass


def _insert_new_task(task: Task) -> None:
    """
    Insert a new task into the storage file.
    Create the file when it is not created.

    Args:
        task        task to be inserted
    """
    new_line = _convert_task_to_line(task)
    open_mode = 'a' if _storage_file_exists() else 'w'

    with open(config.STORAGE_PATH, open_mode) as storage:
        storage.write(new_line)


def _update_task(task: Task) -> None:
    """Override a given task into the storage."""
    new_lines = []

    with open(config.STORAGE_PATH) as storage:
        for line in storage.readlines():
            other_task = _convert_line_to_task(line)

            if task.id == other_task.id:
                line = _convert_task_to_line(task)

            new_lines.append(line)

    with open(config.STORAGE_PATH, 'w') as storage:
        storage.writelines(new_lines)


def _get_next_id() -> str:
    """Return the next id based on the last saved it."""
    return str(int(_get_last_id()) + 1)


def _get_last_id() -> str:
    """Return the last saved it or 0."""
    if _storage_file_exists():
        with open(config.STORAGE_PATH, 'r+') as storage:
            readlines = storage.readlines()
            if len(readlines):
                task = _convert_line_to_task(readlines[-1])
                return task.id
    return '0'


def _storage_file_exists() -> bool:
    return os.path.exists(config.STORAGE_PATH)


def _convert_task_to_line(task: Task) -> str:
    """
    Convert a task instance to a line in the record file.

    Args:
        task      A task instance to be converted

    Return
        A line following the template:

            {task.id}{sep}{task.message}{sep}
            {task.time}{sep}
            {task.project or ''}{sep}
            {task.category or ''}{sep}
            {task.links or ''}{sep}
            {task.started_at or ''}{sep}
            {task.finished_at or ''}
    """
    line = (
        f"{task.id}{sep}{task.message}"
        f"{sep}{task.time}"
        f"{sep}{task.project or ''}"
        f"{sep}{task.category or ''}"
        f"{sep}{task.links or ''}"
        f"{sep}{task.started_at or ''}"
        f"{sep}{task.finished_at or ''}\n"
    )
    return line


def _convert_line_to_task(line: str) -> Task:
    """
    Convert a line record to a task instance.

    Args:
        line       A record line from the storage file

    Return
        A task instance
    """
    id, message, time, project, category, links, started_at, finished_at = line.strip().split(sep)
    return Task(
        id=id,
        message=message,
        time=time,
        category=category,
        project=project,
        links=links,
        started_at=started_at,
        finished_at=finished_at,
    )
