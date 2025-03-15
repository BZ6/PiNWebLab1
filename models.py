from enum import Enum
from typing import Optional

#from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


class RaceType(Enum):
    director = "director"
    worker = "worker"
    junior = "junior"


class SkillWarriorLink(SQLModel, table=True):
    skill_id: int | None = Field(
        default=None, foreign_key="skill.id", primary_key=True
    )
    warrior_id: int | None = Field(
        default=None, foreign_key="warrior.id", primary_key=True
    )
    level: int | None


class SkillDefault(SQLModel):
    name: str
    description: str | None = ""
    
class SkillWarriors(SkillDefault):
    warriors: list["Warrior"] | None = None

class Skill(SkillDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    warriors: list["Warrior"] | None = Relationship(back_populates="skills",
                                                    sa_relationship_kwargs={"cascade": "delete"}, 
                                                    link_model=SkillWarriorLink)

class ProfessionDefault(SQLModel):
    title: str
    description: str

class Profession(ProfessionDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    warriors_prof: list["Warrior"] = Relationship(back_populates="profession",
                                                  sa_relationship_kwargs={"cascade": "delete"})

class WarriorDefault(SQLModel):
    race: RaceType
    name: str
    level: int
    profession_id: int | None = Field(default=None, foreign_key="profession.id")

class WarriorProfessionsAndSkills(WarriorDefault):
    profession: Profession | None = None
    skills: list[Skill] | None = None

class Warrior(WarriorDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    profession: Profession | None = Relationship(back_populates="warriors_prof")
    skills: list[Skill] | None = Relationship(back_populates="warriors",
                                              sa_relationship_kwargs={"cascade": "delete"},
                                              link_model=SkillWarriorLink)
