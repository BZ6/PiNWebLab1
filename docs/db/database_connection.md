# Connection to database

Database connection is established using SQLModel and SQLAlchemy. The connection is configured using environment variables.

## connection.py

```python
from sqlmodel import SQLModel, Session, create_engine
from models.models import User, Priority, Task, ScheduleTask, TimeEntry, Schedule, Notification
import os
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv('DB_ADMIN')
engine = create_engine(db_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
```
