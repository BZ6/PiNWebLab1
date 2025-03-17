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
    """
    Create a new user.

    - **user**: UserDefault object containing user details.
    - **session**: Database session dependency.

    Returns:
        Response[User]: The created user.
    """
    return create_object(session, user, User)

@app.get("/users")
def get_users(session=Depends(get_session)) -> list[User]:
    """
    Get a list of all users.

    - **session**: Database session dependency.

    Returns:
        list[User]: List of users.
    """
    return read_object_list(session, User)

@app.get("/users/{user_id}", response_model=UserInner)
def get_user(user_id: int, session=Depends(get_session)) -> User:
    """
    Get a user by ID.

    - **user_id**: ID of the user to retrieve.
    - **session**: Database session dependency.

    Returns:
        User: The user with the specified ID.
    """
    return read_object(session, user_id, User)

@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserDefault, session=Depends(get_session)) -> UserDefault:
    """
    Update a user by ID.

    - **user_id**: ID of the user to update.
    - **user**: UserDefault object containing updated user details.
    - **session**: Database session dependency.

    Returns:
        UserDefault: The updated user.
    """
    return update_object(session, user_id, user, User)

@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, session=Depends(get_session)) -> dict:
    """
    Delete a user by ID.

    - **user_id**: ID of the user to delete.
    - **session**: Database session dependency.

    Returns:
        dict: A dictionary indicating the result of the deletion.
    """
    return delete_object(session, user_id, User)

# CRUD for Priority
@app.post("/priorities")
def create_priority(priority: PriorityDefault, session=Depends(get_session)) -> Response[Priority]:
    """
    Create a new priority.

    - **priority**: PriorityDefault object containing priority details.
    - **session**: Database session dependency.

    Returns:
        Response[Priority]: The created priority.
    """
    return create_object(session, priority, Priority)

@app.get("/priorities")
def get_priorities(session=Depends(get_session)) -> list[Priority]:
    """
    Get a list of all priorities.

    - **session**: Database session dependency.

    Returns:
        list[Priority]: List of priorities.
    """
    return read_object_list(session, Priority)

@app.get("/priorities/{priority_id}", response_model=PriorityInner)
def get_priority(priority_id: int, session=Depends(get_session)) -> Priority:
    """
    Get a priority by ID.

    - **priority_id**: ID of the priority to retrieve.
    - **session**: Database session dependency.

    Returns:
        Priority: The priority with the specified ID.
    """
    return read_object(session, priority_id, Priority)

@app.patch("/priorities/{priority_id}")
def update_priority(priority_id: int, priority: PriorityDefault, session=Depends(get_session)) -> PriorityDefault:
    """
    Update a priority by ID.

    - **priority_id**: ID of the priority to update.
    - **priority**: PriorityDefault object containing updated priority details.
    - **session**: Database session dependency.

    Returns:
        PriorityDefault: The updated priority.
    """
    return update_object(session, priority_id, priority, Priority)

@app.delete("/priorities/{priority_id}")
def delete_priority(priority_id: int, session=Depends(get_session)) -> dict:
    """
    Delete a priority by ID.

    - **priority_id**: ID of the priority to delete.
    - **session**: Database session dependency.

    Returns:
        dict: A dictionary indicating the result of the deletion.
    """
    return delete_object(session, priority_id, Priority)

# CRUD for Task
@app.post("/tasks")
def create_task(task: TaskDefault, session=Depends(get_session)) -> Response[Task]:
    """
    Create a new task.

    - **task**: TaskDefault object containing task details.
    - **session**: Database session dependency.

    Returns:
        Response[Task]: The created task.
    """
    return create_object(session, task, Task)

@app.get("/tasks")
def get_tasks(session=Depends(get_session)) -> list[Task]:
    """
    Get a list of all tasks.

    - **session**: Database session dependency.

    Returns:
        list[Task]: List of tasks.
    """
    return read_object_list(session, Task)

@app.get("/tasks/{task_id}", response_model=TaskInner)
def get_task(task_id: int, session=Depends(get_session)) -> Task:
    """
    Get a task by ID.

    - **task_id**: ID of the task to retrieve.
    - **session**: Database session dependency.

    Returns:
        Task: The task with the specified ID.
    """
    return read_object(session, task_id, Task)

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: TaskDefault, session=Depends(get_session)) -> TaskDefault:
    """
    Update a task by ID.

    - **task_id**: ID of the task to update.
    - **task**: TaskDefault object containing updated task details.
    - **session**: Database session dependency.

    Returns:
        TaskDefault: The updated task.
    """
    return update_object(session, task_id, task, Task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session=Depends(get_session)) -> dict:
    """
    Delete a task by ID.

    - **task_id**: ID of the task to delete.
    - **session**: Database session dependency.

    Returns:
        dict: A dictionary indicating the result of the deletion.
    """
    return delete_object(session, task_id, Task)

# CRUD for TimeEntry
@app.post("/time_entries")
def create_time_entry(time_entry: TimeEntryDefault, session=Depends(get_session)) -> Response[TimeEntry]:
    """
    Create a new time entry.

    - **time_entry**: TimeEntryDefault object containing time entry details.
    - **session**: Database session dependency.

    Returns:
        Response[TimeEntry]: The created time entry.
    """
    return create_object(session, time_entry, TimeEntry)

@app.get("/time_entries")
def get_time_entries(session=Depends(get_session)) -> list[TimeEntry]:
    """
    Get a list of all time entries.

    - **session**: Database session dependency.

    Returns:
        list[TimeEntry]: List of time entries.
    """
    return read_object_list(session, TimeEntry)

@app.get("/time_entries/{time_entry_id}", response_model=TimeEntryInner)
def get_time_entry(time_entry_id: int, session=Depends(get_session)) -> TimeEntry:
    """
    Get a time entry by ID.

    - **time_entry_id**: ID of the time entry to retrieve.
    - **session**: Database session dependency.

    Returns:
        TimeEntry: The time entry with the specified ID.
    """
    return read_object(session, time_entry_id, TimeEntry)

@app.patch("/time_entries/{time_entry_id}")
def update_time_entry(time_entry_id: int, time_entry: TimeEntryDefault, session=Depends(get_session)) -> TimeEntryDefault:
    """
    Update a time entry by ID.

    - **time_entry_id**: ID of the time entry to update.
    - **time_entry**: TimeEntryDefault object containing updated time entry details.
    - **session**: Database session dependency.

    Returns:
        TimeEntryDefault: The updated time entry.
    """
    return update_object(session, time_entry_id, time_entry, TimeEntry)

@app.delete("/time_entries/{time_entry_id}")
def delete_time_entry(time_entry_id: int, session=Depends(get_session)) -> dict:
    """
    Delete a time entry by ID.

    - **time_entry_id**: ID of the time entry to delete.
    - **session**: Database session dependency.

    Returns:
        dict: A dictionary indicating the result of the deletion.
    """
    return delete_object(session, time_entry_id, TimeEntry)

# CRUD for Schedule
@app.post("/schedules")
def create_schedule(schedule: ScheduleDefault, session=Depends(get_session)) -> Response[Schedule]:
    """
    Create a new schedule.

    - **schedule**: ScheduleDefault object containing schedule details.
    - **session**: Database session dependency.

    Returns:
        Response[Schedule]: The created schedule.
    """
    return create_object(session, schedule, Schedule)

@app.get("/schedules")
def get_schedules(session=Depends(get_session)) -> list[Schedule]:
    """
    Get a list of all schedules.

    - **session**: Database session dependency.

    Returns:
        list[Schedule]: List of schedules.
    """
    return read_object_list(session, Schedule)

@app.get("/schedules/{schedule_id}", response_model=ScheduleInner)
def get_schedule(schedule_id: int, session=Depends(get_session)) -> Schedule:
    """
    Get a schedule by ID.

    - **schedule_id**: ID of the schedule to retrieve.
    - **session**: Database session dependency.

    Returns:
        Schedule: The schedule with the specified ID.
    """
    return read_object(session, schedule_id, Schedule)

@app.patch("/schedules/{schedule_id}")
def update_schedule(schedule_id: int, schedule: ScheduleDefault, session=Depends(get_session)) -> ScheduleDefault:
    """
    Update a schedule by ID.

    - **schedule_id**: ID of the schedule to update.
    - **schedule**: ScheduleDefault object containing updated schedule details.
    - **session**: Database session dependency.

    Returns:
        ScheduleDefault: The updated schedule.
    """
    return update_object(session, schedule_id, schedule, Schedule)

@app.delete("/schedules/{schedule_id}")
def delete_schedule(schedule_id: int, session=Depends(get_session)) -> dict:
    """
    Delete a schedule by ID.

    - **schedule_id**: ID of the schedule to delete.
    - **session**: Database session dependency.

    Returns:
        dict: A dictionary indicating the result of the deletion.
    """
    return delete_object(session, schedule_id, Schedule)

# CRUD for Notification
@app.post("/notifications")
def create_notification(notification: NotificationDefault, session=Depends(get_session)) -> Response[Notification]:
    """
    Create a new notification.

    - **notification**: NotificationDefault object containing notification details.
    - **session**: Database session dependency.

    Returns:
        Response[Notification]: The created notification.
    """
    return create_object(session, notification, Notification)

@app.get("/notifications")
def get_notifications(session=Depends(get_session)) -> list[Notification]:
    """
    Get a list of all notifications.

    - **session**: Database session dependency.

    Returns:
        list[Notification]: List of notifications.
    """
    return read_object_list(session, Notification)

@app.get("/notifications/{notification_id}", response_model=NotificationInner)
def get_notification(notification_id: int, session=Depends(get_session)) -> Notification:
    """
    Get a notification by ID.

    - **notification_id**: ID of the notification to retrieve.
    - **session**: Database session dependency.

    Returns:
        Notification: The notification with the specified ID.
    """
    return read_object(session, notification_id, Notification)

@app.patch("/notifications/{notification_id}")
def update_notification(notification_id: int, notification: NotificationDefault, session=Depends(get_session)) -> NotificationDefault:
    """
    Update a notification by ID.

    - **notification_id**: ID of the notification to update.
    - **notification**: NotificationDefault object containing updated notification details.
    - **session**: Database session dependency.

    Returns:
        NotificationDefault: The updated notification.
    """
    return update_object(session, notification_id, notification, Notification)

@app.delete("/notifications/{notification_id}")
def delete_notification(notification_id: int, session=Depends(get_session)) -> dict:
    """
    Delete a notification by ID.

    - **notification_id**: ID of the notification to delete.
    - **session**: Database session dependency.

    Returns:
        dict: A dictionary indicating the result of the deletion.
    """
    return delete_object(session, notification_id, Notification)

# CRUD for ScheduleTask
@app.post("/schedule_tasks/{schedule_id}/{task_id}")
def create_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> Response[ScheduleTask]:
    """
    Create a new schedule task.

    - **schedule_id**: ID of the schedule.
    - **task_id**: ID of the task.
    - **session**: Database session dependency.

    Returns:
        Response[ScheduleTask]: The created schedule task.
    """
    return create_st(schedule_id, task_id, session)

@app.get("/schedule_tasks")
def get_schedule_tasks(session=Depends(get_session)) -> list[ScheduleTask]:
    """
    Get a list of all schedule tasks.

    - **session**: Database session dependency.

    Returns:
        list[ScheduleTask]: List of schedule tasks.
    """
    return read_object_list(session, ScheduleTask)

@app.get("/schedule_tasks/{schedule_id}/{task_id}")
def get_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> ScheduleTask:
    """
    Get a schedule task by schedule ID and task ID.

    - **schedule_id**: ID of the schedule.
    - **task_id**: ID of the task.
    - **session**: Database session dependency.

    Returns:
        ScheduleTask: The schedule task with the specified IDs.
    """
    return get_st(schedule_id, task_id, session)

@app.delete("/schedule_tasks/{schedule_id}/{task_id}")
def delete_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> dict:
    """
    Delete a schedule task by schedule ID and task ID.

    - **schedule_id**: ID of the schedule.
    - **task_id**: ID of the task.
    - **session**: Database session dependency.

    Returns:
        dict: A dictionary indicating the result of the deletion.
    """
    return delete_st(schedule_id, task_id, session)
