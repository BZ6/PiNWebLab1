from fastapi import APIRouter, Depends

from src.api.generic import Response, create_object, delete_object, read_object, read_object_list, update_object
from src.db.connection import get_session
from src.api.users import routes as users
from src.api.priorities import routes as priorities
from src.api.notifications import routes as notifications
from src.api.schedules import routes as schedules
from src.api.tasks import routes as tasks
from src.api.time_entries import routes as time_entries
from src.api.schedule_tasks import routes as schedule_tasks


router = APIRouter()


router.include_router(users.router)
router.include_router(priorities.router)
router.include_router(notifications.router)
router.include_router(schedules.router)
router.include_router(tasks.router)
router.include_router(time_entries.router)
router.include_router(schedule_tasks.router)
