from fastapi import FastAPI

from typing import TypedDict
from models import Warrior, Profession

app = FastAPI()

temp_bd = [
{
    "id": 1,
    "race": "director",
    "name": "Мартынов Дмитрий",
    "level": 12,
    "profession": {
        "id": 1,
        "title": "Влиятельный человек",
        "description": "Эксперт по всем вопросам"
    },
    "skills":
        [{
            "id": 1,
            "name": "Купле-продажа компрессоров",
            "description": ""
        },
        {
            "id": 2,
            "name": "Оценка имущества",
            "description": ""

        }]
},
{
    "id": 2,
    "race": "worker",
    "name": "Андрей Косякин",
    "level": 12,
    "profession": {
        "id": 1,
        "title": "Дельфист-гребец",
        "description": "Уважаемый сотрудник"
    },
    "skills": []
},
]

@app.get("/")
def hello():
    return "Hello, [username]!"

@app.get("/warriors_list")
def warriors_list() -> list[Warrior]:
    return temp_bd


@app.get("/warrior/{warrior_id}")
def warriors_get(warrior_id: int) -> list[Warrior]:
    return [warrior for warrior in temp_bd if warrior.get("id") == warrior_id]


@app.get("/warrior/{warrior_id}/profession")
def profession_of_warriors_get(warrior_id: int) -> list[Profession]:
    return [warrior.get("profession") for warrior in temp_bd if warrior.get("id") == warrior_id]


@app.post("/warrior")
def warriors_create(warrior: Warrior) -> TypedDict('Response', {"status": int, "data": Warrior}):
    warrior_to_append = warrior.model_dump()
    temp_bd.append(warrior_to_append)
    return {"status": 200, "data": warrior}


@app.delete("/warrior/delete{warrior_id}")
def warrior_delete(warrior_id: int):
    for i, warrior in enumerate(temp_bd):
        if warrior.get("id") == warrior_id:
            temp_bd.pop(i)
            break
    return {"status": 201, "message": "deleted"}


@app.put("/warrior{warrior_id}")
def warrior_update(warrior_id: int, warrior: Warrior) -> list[Warrior]:
    for war in temp_bd:
        if war.get("id") == warrior_id:
            warrior_to_append = warrior.model_dump()
            temp_bd.remove(war)
            temp_bd.append(warrior_to_append)
    return temp_bd

@app.put("/warrior{warrior_id}/profession")
def warrior_update(warrior_id: int, profession: Profession) -> list[Warrior]:
    for war in temp_bd:
        if war.get("id") == warrior_id:
            profession_to_update = profession.model_dump()
            warrior_to_append = war.copy()
            warrior_to_append.pop("profession")
            warrior_to_append["profession"] = profession_to_update
            temp_bd.remove(war)
            temp_bd.append(warrior_to_append)
    return temp_bd
