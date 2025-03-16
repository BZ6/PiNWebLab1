from fastapi import Depends, FastAPI

from api.generic import create_object, read_object_list, delete_object, read_object, update_object, Response
from api.schedule_tasks import create_st, delete_st, get_st
from connection import init_db, get_session
from models.default import NotificationDefault, ScheduleDefault, TaskDefault, PriorityDefault, TimeEntryDefault, UserDefault
from models.models import NotificationInner, PriorityInner, ScheduleInner, TaskInner, TimeEntryInner, User, Priority, Task, ScheduleTask, TimeEntry, Schedule, Notification, UserInner

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# CRUD for User
@app.post("/users")
def create_user(user: UserDefault, session=Depends(get_session)) -> Response[User]:
    return create_object(session, user, User)

@app.get("/users")
def get_users(session=Depends(get_session)) -> list[User]:
    return read_object_list(session, User)

@app.get("/users/{user_id}", response_model=UserInner)
def get_user(user_id: int, session=Depends(get_session)) -> User:
    return read_object(session, user_id, User)

@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserDefault, session=Depends(get_session)) -> UserDefault:
    return update_object(session, user_id, user, User)

@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, user_id, User)

# CRUD for Priority
@app.post("/priorities")
def create_priority(priority: PriorityDefault, session=Depends(get_session)) -> Response[Priority]:
    return create_object(session, priority, Priority)

@app.get("/priorities")
def get_priorities(session=Depends(get_session)) -> list[Priority]:
    return read_object_list(session, Priority)

@app.get("/priorities/{priority_id}", response_model=PriorityInner)
def get_priority(priority_id: int, session=Depends(get_session)) -> Priority:
    return read_object(session, priority_id, Priority)

@app.patch("/priorities/{priority_id}")
def update_user(priority_id: int, priority: PriorityDefault, session=Depends(get_session)) -> PriorityDefault:
    return update_object(session, priority_id, priority, Priority)

@app.delete("/priorities/{priority_id}")
def delete_user(priority_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, priority_id, Priority)

# CRUD for Task
@app.post("/tasks")
def create_task(task: TaskDefault, session=Depends(get_session)) -> Response[Task]:
    return create_object(session, task, Task)

@app.get("/tasks")
def get_tasks(session=Depends(get_session)) -> list[Task]:
    return read_object_list(session, Task)

@app.get("/tasks/{task_id}", response_model=TaskInner)
def get_task(task_id: int, session=Depends(get_session)) -> Task:
    return read_object(session, task_id, Task)

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: TaskDefault, session=Depends(get_session)) -> TaskDefault:
    return update_object(session, task_id, task, Task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, task_id, Task)

# CRUD for TimeEntry
@app.post("/time_entries")
def create_time_entry(time_entry: TimeEntryDefault, session=Depends(get_session)) -> Response[TimeEntry]:
    return create_object(session, time_entry, TimeEntry)

@app.get("/time_entries")
def get_time_entries(session=Depends(get_session)) -> list[TimeEntry]:
    return read_object_list(session, TimeEntry)

@app.get("/time_entries/{time_entry_id}", response_model=TimeEntryInner)
def get_time_entry(time_entry_id: int, session=Depends(get_session)) -> TimeEntry:
    return read_object(session, time_entry_id, TimeEntry)

@app.patch("/time_entries/{ustime_entry_ider_id}")
def update_time_entry(time_entry_id: int, time_entry: TimeEntryDefault, session=Depends(get_session)) -> TimeEntryDefault:
    return update_object(session, time_entry_id, time_entry, TimeEntry)

@app.delete("/time_entries/{ustime_entry_ider_id}")
def delete_time_entry(ustime_entry_ider_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, ustime_entry_ider_id, TimeEntry)

# CRUD for Schedule
@app.post("/schedules")
def create_schedule(schedule: ScheduleDefault, session=Depends(get_session)) -> Response[Schedule]:
    return create_object(session, schedule, Schedule)

@app.get("/schedules")
def get_schedules(session=Depends(get_session)) -> list[Schedule]:
    return read_object_list(session, Schedule)

@app.get("/schedules/{schedule_id}", response_model=ScheduleInner)
def get_schedule(schedule_id: int, session=Depends(get_session)) -> Schedule:
    return read_object(session, schedule_id, Schedule)

@app.patch("/schedules/{schedule_id}")
def update_schedule(schedule_id: int, schedule: ScheduleDefault, session=Depends(get_session)) -> ScheduleDefault:
    return update_object(session, schedule_id, schedule, Schedule)

@app.delete("/schedules/{schedule_id}")
def delete_schedule(schedule_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, schedule_id, Schedule)

# CRUD for Notification
@app.post("/notifications")
def create_notification(notification: NotificationDefault, session=Depends(get_session)) -> Response[Notification]:
    return create_object(session, notification, Notification)

@app.get("/notifications")
def get_notifications(session=Depends(get_session)) -> list[Notification]:
    return read_object_list(session, Notification)

@app.get("/notifications/{notification_id}", response_model=NotificationInner)
def get_notification(notification_id: int, session=Depends(get_session)) -> Notification:
    return read_object(session, notification_id, Notification)

@app.patch("/notifications/{notification_id}")
def update_notification(notification_id: int, notification: NotificationDefault, session=Depends(get_session)) -> NotificationDefault:
    return update_object(session, notification_id, notification, Notification)

@app.delete("/notifications/{notification_id}")
def delete_notification(notification_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, notification_id, Notification)

# CRUD for ScheduleTask
@app.post("/schedule_tasks/{schedule_id}/{task_id}")
def create_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> Response[ScheduleTask]:
    return create_st(schedule_id, task_id, session)

@app.get("/schedule_tasks")
def get_schedule_tasks(session=Depends(get_session)) -> list[ScheduleTask]:
    return read_object_list(session, ScheduleTask)

@app.get("/schedule_tasks/{schedule_id}/{task_id}")
def get_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> ScheduleTask:
    return get_st(schedule_id, task_id, session)

@app.delete("/schedule_tasks/{schedule_id}/{task_id}")
def delete_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> dict:
    return delete_st(schedule_id, task_id, session)
