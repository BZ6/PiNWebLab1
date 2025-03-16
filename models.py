from typing import TypeVar
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

# Define types for Generic
InputModel = TypeVar('InputModel', bound=SQLModel)
OutputModel = TypeVar('OutputModel', bound=SQLModel)

# Associative table
class ScheduleTaskDefault(SQLModel):
    schedule_id: int | None = Field(default=None, foreign_key="schedule.id", primary_key=True)
    task_id: int | None = Field(default=None, foreign_key="task.id", primary_key=True)

class ScheduleTask(ScheduleTaskDefault, table=True):
    added_at: datetime = Field(default_factory=datetime.utcnow)

# User table
class UserDefault(SQLModel):
    username: str
    email: str

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
class PriorityDefault(SQLModel):
    name: str

class PriorityInner(PriorityDefault):
    tasks: list["Task"] | None = None

class Priority(PriorityDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tasks: list["Task"] = Relationship(back_populates="priority",
                                       sa_relationship_kwargs={"cascade": "delete"})

# Task table
class TaskDefault(SQLModel):
    description: str
    deadline: datetime
    priority_id: int | None = Field(default=None, foreign_key="priority.id")
    user_id: int | None = Field(default=None, foreign_key="user.id")

class TaskInner(TaskDefault):
    priority: Priority | None = None
    user: list[User] | None = None
    time_entries: list["TimeEntry"] | None = None
    notifications: list["Notification"] | None = None
    schedules: list["Schedule"] | None = None

class Task(TaskDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    priority: Priority | None = Relationship(back_populates="tasks")
    user: list[User] = Relationship(back_populates="tasks")
    time_entries: list["TimeEntry"] = Relationship(back_populates="task",
                                                   sa_relationship_kwargs={"cascade": "delete"})
    notifications: list["Notification"] = Relationship(back_populates="task",
                                                       sa_relationship_kwargs={"cascade": "delete"})
    schedules: list["Schedule"] = Relationship(back_populates="tasks",
                                               link_model=ScheduleTask,
                                               sa_relationship_kwargs={"cascade": "delete"})


# TimeEntry table
class TimeEntryDefault(SQLModel):
    task_id: int | None = Field(default=None, foreign_key="task.id")
    start_time: datetime
    end_time: datetime
    duration: int

class TimeEntryInner(TimeEntryDefault):
    task: Task | None = None

class TimeEntry(TimeEntryDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task: Task | None = Relationship(back_populates="time_entries")

# Schedule table
class ScheduleDefault(SQLModel):
    user_id: int | None = Field(default=None, foreign_key="user.id")
    date: datetime

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
class NotificationDefault(SQLModel):
    task_id: int | None = Field(default=None, foreign_key="task.id")
    message: str
    sent_at: datetime

class NotificationInner(NotificationDefault):
    task: Task | None = None

class Notification(NotificationDefault, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task: Task | None = Relationship(back_populates="notifications")
