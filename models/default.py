from typing import TypeVar
from sqlmodel import SQLModel, Field
from datetime import datetime

# Define types for Generic
InputModel = TypeVar('InputModel', bound=SQLModel)
OutputModel = TypeVar('OutputModel', bound=SQLModel)

# Associative table
class ScheduleTaskDefault(SQLModel):
    schedule_id: int | None = Field(default=None, foreign_key="schedule.id", primary_key=True)
    task_id: int | None = Field(default=None, foreign_key="task.id", primary_key=True)

# User table
class UserDefault(SQLModel):
    username: str
    email: str

# Priority table
class PriorityDefault(SQLModel):
    name: str

# Task table
class TaskDefault(SQLModel):
    description: str
    deadline: datetime
    priority_id: int | None = Field(default=None, foreign_key="priority.id")
    user_id: int | None = Field(default=None, foreign_key="user.id")

# TimeEntry table
class TimeEntryDefault(SQLModel):
    task_id: int | None = Field(default=None, foreign_key="task.id")
    start_time: datetime
    end_time: datetime
    duration: int

# Schedule table
class ScheduleDefault(SQLModel):
    user_id: int | None = Field(default=None, foreign_key="user.id")
    date: datetime

# Notification table
class NotificationDefault(SQLModel):
    task_id: int | None = Field(default=None, foreign_key="task.id")
    message: str
    sent_at: datetime
