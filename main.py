from typing import TypedDict
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import select

from connection import get_session, init_db
from models import Profession, ProfessionDefault, Skill, SkillDefault, SkillWarriorLink, SkillWarriors, Warrior, WarriorDefault, WarriorProfessionsAndSkills

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def hello():
    return "Hello, [username]!"

@app.post("/warrior")
def warriors_create(warrior: WarriorDefault, session=Depends(get_session)) -> TypedDict('Response', {"status": int, "data": Warrior}):
    warrior = Warrior.model_validate(warrior)
    session.add(warrior)
    session.commit()
    session.refresh(warrior)
    return {"status": 200, "data": warrior}

@app.get("/warriors_list")
def warriors_list(session=Depends(get_session)) -> list[Warrior]:
    return session.exec(select(Warrior)).all()


@app.get("/warrior/{warrior_id}", response_model=WarriorProfessionsAndSkills)
def warriors_get(warrior_id: int, session=Depends(get_session)) -> Warrior:
    warrior = session.get(Warrior, warrior_id)
    return warrior

@app.patch("/warrior{warrior_id}")
def warrior_update(warrior_id: int, warrior: WarriorDefault, session=Depends(get_session)) -> WarriorDefault:
    db_warrior = session.get(Warrior, warrior_id)
    if not db_warrior:
        raise HTTPException(status_code=404, detail="Warrior not found")
    warrior_data = warrior.model_dump(exclude_unset=True)
    for key, value in warrior_data.items():
        setattr(db_warrior, key, value)
    session.add(db_warrior)
    session.commit()
    session.refresh(db_warrior)
    return db_warrior

@app.delete("/warrior/delete{warrior_id}")
def warrior_delete(warrior_id: int, session=Depends(get_session)):
    warrior = session.get(Warrior, warrior_id)
    if not warrior:
        raise HTTPException(status_code=404, detail="Warrior not found")
    session.delete(warrior)
    session.commit()
    return {"ok": True}


@app.get("/professions_list")
def professions_list(session=Depends(get_session)) -> list[Profession]:
    return session.exec(select(Profession)).all()

@app.get("/profession/{profession_id}")
def profession_get(profession_id: int, session=Depends(get_session)) -> Profession:
    return session.get(Profession, profession_id)

@app.post("/profession")
def profession_create(prof: ProfessionDefault, session=Depends(get_session)) -> TypedDict('Response', {"status": int, "data": Profession}):
    prof = Profession.model_validate(prof)
    session.add(prof)
    session.commit()
    session.refresh(prof)
    return {"status": 200, "data": prof}


@app.get("/skills_list")
def professions_list(session=Depends(get_session)) -> list[Skill]:
    return session.exec(select(Skill)).all()

@app.get("/skill/{skill_id}", response_model=SkillWarriors)
def skill_get(skill_id: int, session=Depends(get_session)) -> Skill:
    skill = session.get(Skill, skill_id)
    return skill

@app.post("/skill")
def skill_create(skill: SkillDefault, session=Depends(get_session)) -> TypedDict('Response', {"status": int, "data": Skill}):
    skill = Skill.model_validate(skill)
    session.add(skill)
    session.commit()
    session.refresh(skill)
    return {"status": 200, "data": skill}

@app.patch("/skill{skill_id}")
def skill_update(skill_id: int, skill: SkillDefault, session=Depends(get_session)) -> SkillDefault:
    db_skill = session.get(Skill, skill_id)
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    skill_data = skill.model_dump(exclude_unset=True)
    for key, value in skill_data.items():
        setattr(db_skill, key, value)
    session.add(db_skill)
    session.commit()
    session.refresh(db_skill)
    return db_skill

@app.delete("/skill/delete{skill_id}")
def skill_delete(skill_id: int, session=Depends(get_session)):
    skill = session.get(Skill, skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    session.delete(skill)
    session.commit()
    return {"ok": True}

@app.post("/link/warrior{warrior_id}/skill{skill_id}")
def link_warrior_skill_create(warrior_id: int, skill_id: int, session=Depends(get_session)):
    warrior = session.get(Warrior, warrior_id)
    skill = session.get(Skill, skill_id)

    if not warrior or not skill:
        raise HTTPException(status_code=404, detail="Warrior or Skill not found")
    
    warrior_skill_link = SkillWarriorLink(warrior_id=warrior_id, skill_id=skill_id)

    session.add(warrior_skill_link)
    session.commit()
    session.refresh(warrior_skill_link)

    return {"status": 200, "data": warrior_skill_link}

@app.delete("/link/remove/warrior{warrior_id}/skill{skill_id}")
def link_warrior_skill_delete(warrior_id: int, skill_id: int, session=Depends(get_session)):
    statement = select(SkillWarriorLink).where(
        SkillWarriorLink.warrior_id == warrior_id,
        SkillWarriorLink.skill_id == skill_id
    )
    result = session.exec(statement)
    print(result)
    warrior_skill_link = result.one_or_none()

    if not warrior_skill_link:
        raise HTTPException(status_code=404, detail="Link between Warrior and Skill not found")

    session.delete(warrior_skill_link)
    session.commit()

    return {"ok": True}
