from sqlmodel import SQLModel, Session, create_engine

from models import Profession, Skill, SkillWarriorLink, Warrior

with open('.pgpass', 'r') as pass_file:
    password = pass_file.read()

db_url = f"postgresql://postgres:{password}@localhost/warriors_db"
engine = create_engine(db_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
