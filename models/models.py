from sqlmodel import Field, Relationship
from datetime import datetime

from models.default import NotificationDefault, PriorityDefault, ScheduleDefault, ScheduleTaskDefault, TaskDefault, TimeEntryDefault, UserDefault

# Associative table
class ScheduleTask(ScheduleTaskDefault, table=True):
    added_at: datetime = Field(default_factory=datetime.utcnow)

# User table
class UserInner(UserDefault):
    tasks: list["Task"] | None = None
    schedules: list["Schedule"] | None = None

class User(UserDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tasks: list["Task"] = Relationship(back_populates="user",
                                       sa_relationship_kwargs={"cascade": "delete"})
    schedules: list["Schedule"] = Relationship(back_populates="user",
                                               sa_relationship_kwargs={"cascade": "delete"})

# Priority table
class PriorityInner(PriorityDefault):
    tasks: list["Task"] | None = None

class Priority(PriorityDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tasks: list["Task"] = Relationship(back_populates="priority",
                                       sa_relationship_kwargs={"cascade": "delete"})

# Task table
class TaskInner(TaskDefault):
    priority: Priority | None = None
    user: User | None = None
    time_entries: list["TimeEntry"] | None = None
    notifications: list["Notification"] | None = None
    schedules: list["Schedule"] | None = None

class Task(TaskDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    priority: Priority | None = Relationship(back_populates="tasks")
    user: User | None = Relationship(back_populates="tasks")
    time_entries: list["TimeEntry"] = Relationship(back_populates="task",
                                                   sa_relationship_kwargs={"cascade": "delete"})
    notifications: list["Notification"] = Relationship(back_populates="task",
                                                       sa_relationship_kwargs={"cascade": "delete"})
    schedules: list["Schedule"] = Relationship(back_populates="tasks",
                                               link_model=ScheduleTask,
                                               sa_relationship_kwargs={"cascade": "delete"})


# TimeEntry table
class TimeEntryInner(TimeEntryDefault):
    task: Task | None = None

class TimeEntry(TimeEntryDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task: Task | None = Relationship(back_populates="time_entries")

# Schedule table
class ScheduleInner(ScheduleDefault):
    user: User | None = None
    tasks: list[Task] | None = None
    
class Schedule(ScheduleDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: User | None = Relationship(back_populates="schedules")
    tasks: list[Task] = Relationship(back_populates="schedules",
                                     link_model=ScheduleTask,
                                     sa_relationship_kwargs={"cascade": "delete"})

# Notification table
class NotificationInner(NotificationDefault):
    task: Task | None = None

class Notification(NotificationDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task: Task | None = Relationship(back_populates="notifications")
