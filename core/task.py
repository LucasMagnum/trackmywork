import datetime
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)


class Task:
    """
    A Task representation.

    A task our core entity and it has some methods to start, finish and
    edit itself.
    """
    read_only_fields = ['started_at', 'finished_at']

    def __init__(self, id, message, time, category, links, project, started_at, finished_at):
        self.id = id
        self.message = message
        self.time = time
        self.category = category
        self.project = project
        self.links = links
        self.started_at = started_at
        self.finished_at = finished_at

    def __repr__(self):
        return f"""
        Task(
            id="{self.id}",
            message="{self.message}",
            time="{self.time}",
            category="{self.category or ''}",
            project="{self.project or ''}",
            links="{self.links or ''}",
            started_at="{self.started_at or ''}",
            finished_at="{self.finished_at or ''}",
        )
        """

    @classmethod
    def create(cls, message, time, category=None, links=None, project=None):
        return cls(
            id=None,
            message=message,
            time=time,
            category=category,
            links=links,
            project=project,
            started_at=None,
            finished_at=None
        )

    def start(self) -> bool:
        """
        Start a task setting the `started_at` attribute.

        Return
            A boolean determining if the task has changed.
        """
        if not self.started_at:
            self.started_at = datetime.datetime.now()
            return True
        return False

    def finish(self) -> bool:
        """
        Finish a task setting the `finished_at` attribute.

        Return
            A boolean determining if the task has changed.
        """
        if not self.finished_at:
            self.finished_at = datetime.datetime.now()
            return True
        return False

    def edit(self, new_values: dict) -> List[Tuple[str, str, str]]:
        """
        Edit a task overriding the new values.

        Args
            new_values: a dict containing the attribute name and its value

        Return:
            A boolean determining if the task has changed and the changed fields.
        """
        fields_changed = []

        for field_name, new_value in new_values.items():
            if field_name in self.read_only_fields:
                logger.warn(f"It is not allowed to change the field {field_name}.")
                continue

            try:
                field_value = getattr(self, field_name)
            except AttributeError:
                logger.warn(f"Task doesn't have the field {field_name}")
                continue

            if new_value is not None and new_value != field_value:
                setattr(self, field_name, new_value)
                fields_changed.append((field_name, field_value, new_value))

        return fields_changed
