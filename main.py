from typing import Type, TypedDict, Generic
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from connection import init_db, get_session
from models import NotificationDefault, NotificationInner, PriorityInner, ScheduleDefault, ScheduleInner, TaskDefault, PriorityDefault, TaskInner, TimeEntryDefault, TimeEntryInner, UserDefault, InputModel, OutputModel, UserInner
from models import User, Priority, Task, ScheduleTask, TimeEntry, Schedule, Notification

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# Response annotation for API
class Response(TypedDict, Generic[OutputModel]):
    status: int
    data: OutputModel

# Generic function for creation object and addition in database
def create_object(session: Session, input_model: InputModel, output_model: Type[OutputModel]) -> Response[OutputModel]:
    output_instance = output_model.model_validate(input_model)
    session.add(output_instance)
    session.commit()
    session.refresh(output_instance)
    return {"status": 201, "data": output_instance}

# Generic function for read object by id from database
def read_object(session: Session, id: int, output_model: Type[OutputModel]) -> OutputModel:
    output_instance = session.get(output_model, id)
    if not output_instance:
        raise HTTPException(status_code=404, detail=f"{output_model.__name__} not found")
    return output_instance

# Generic function for update object by id from database
def update_object(session: Session, id: int, input_model: InputModel, output_model: Type[OutputModel]) -> InputModel:
    output_instance = session.get(output_model, id)
    if not output_instance:
        raise HTTPException(status_code=404, detail=f"{output_model.__name__} not found")
    output_data = input_model.model_dump(exclude_unset=True)
    for key, value in output_data.items():
        setattr(output_instance, key, value)
    session.add(output_instance)
    session.commit()
    session.refresh(output_instance)
    return output_instance

# Generic function for delete object by id from database
def delete_object(session: Session, id: int, output_model: Type[OutputModel]):
    output_instance = session.get(output_model, id)
    if not output_instance:
        raise HTTPException(status_code=404, detail=f"{output_model.__name__} not found")
    session.delete(output_instance)
    session.commit()
    return {"ok": True}

# CRUD for User
@app.post("/users")
def create_user(user: UserDefault, session=Depends(get_session)) -> Response[User]:
    return create_object(session, user, User)

@app.get("/users")
def get_users(session=Depends(get_session)) -> list[User]:
    return session.exec(select(User)).all()

@app.get("/users/{user_id}", response_model=UserInner)
def get_user(user_id: int, session=Depends(get_session)) -> User:
    return read_object(session, user_id, User)

@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserDefault, session=Depends(get_session)) -> UserDefault:
    return update_object(session, user_id, user, User)

@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, user_id, User)

@app.post("/priorities")
def create_priority(priority: PriorityDefault, session=Depends(get_session)) -> Response[Priority]:
    return create_object(session, priority, Priority)

@app.get("/priorities")
def get_priorities(session=Depends(get_session)) -> list[Priority]:
    return session.exec(select(Priority)).all()

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
    return session.exec(select(Task)).all()

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
    return session.exec(select(TimeEntry)).all()

@app.get("/time_entries/{time_entry_id}", response_model=TimeEntryInner)
def get_time_entry(time_entry_id: int, session=Depends(get_session)) -> TimeEntry:
    return read_object(session, time_entry_id, TimeEntry)

@app.patch("/time_entries/{time_entry_ider_id}")
def update_time_entry(time_entry_id: int, time_entry: TimeEntryDefault, session=Depends(get_session)) -> TimeEntryDefault:
    return update_object(session, time_entry_id, time_entry, TimeEntry)

@app.delete("/time_entries/{time_entry_ider_id}")
def delete_time_entry(ustime_entry_ider_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, ustime_entry_ider_id, TimeEntry)

# CRUD for Schedule
@app.post("/schedules")
def create_schedule(schedule: ScheduleDefault, session=Depends(get_session)) -> Response[Schedule]:
    return create_object(session, schedule, Schedule)

@app.get("/schedules")
def get_schedules(session=Depends(get_session)) -> list[Schedule]:
    return session.exec(select(Schedule)).all()

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
    return session.exec(select(Notification)).all()

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
    schedule = session.get(Schedule, schedule_id)
    task = session.get(Task, task_id)
    if not schedule or not task:
        raise HTTPException(status_code=404, detail="Schedule or Task not found")
    schedule_task = ScheduleTask(schedule_id=schedule_id, task_id=task_id)
    session.add(schedule_task)
    session.commit()
    session.refresh(schedule_task)
    return {"status": 201, "data": schedule_task}

@app.get("/schedule_tasks")
def get_schedule_tasks(session=Depends(get_session)) -> list[ScheduleTask]:
    return session.exec(select(ScheduleTask)).all()

@app.get("/schedule_tasks/{schedule_id}/{task_id}")
def get_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> ScheduleTask:
    schedule_task = session.get(ScheduleTask, (schedule_id, task_id))
    if not schedule_task:
        raise HTTPException(status_code=404, detail="Pair Schedule and Task not found")
    return schedule_task

@app.delete("/schedule_tasks/{schedule_id}/{task_id}")
def delete_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> dict:
    schedule_task = session.get(ScheduleTask, (schedule_id, task_id))
    if not schedule_task:
        raise HTTPException(status_code=404, detail="ScheduleTask not found")
    session.delete(schedule_task)
    session.commit()
    return {"ok": True}
