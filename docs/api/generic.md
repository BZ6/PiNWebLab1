# generic.py

The `generic.py` file contains generic functions for performing CRUD (Create, Read, Update, Delete) operations on database objects. These functions are designed to work with SQLModel and FastAPI to provide a flexible and reusable way to interact with different models in the database.

## Functions

- `create_object(session: Session, input_model: InputModel, output_model: Type[OutputModel]) -> Response[OutputModel]`
  - Creates a new object in the database.
  
- `read_object_list(session: Session, output_model: Type[OutputModel]) -> list[OutputModel]`
  - Retrieves a list of all objects from the database.
  
- `read_object(session: Session, id: int, output_model: Type[OutputModel]) -> OutputModel`
  - Retrieves a single object by its ID from the database.
  
- `update_object(session: Session, id: int, input_model: InputModel, output_model: Type[OutputModel]) -> InputModel`
  - Updates an existing object in the database by its ID.
  
- `delete_object(session: Session, id: int, output_model: Type[OutputModel]) -> dict`
  - Deletes an object by its ID from the database.

## Classes

- `Response(TypedDict, Generic[OutputModel])`
  - A generic response class used to standardize API responses.

## Code

```python
from typing import Generic, Type, TypedDict
from fastapi import HTTPException
from sqlmodel import Session, select

from models.default import InputModel, OutputModel

class Response(TypedDict, Generic[OutputModel]):
    status: int
    data: OutputModel

def create_object(session: Session, input_model: InputModel, output_model: Type[OutputModel]) -> Response[OutputModel]:
    output_instance = output_model.model_validate(input_model)
    session.add(output_instance)
    session.commit()
    session.refresh(output_instance)
    return {"status": 201, "data": output_instance}

def read_object_list(session: Session, output_model: Type[OutputModel]) -> list[OutputModel]:
    return session.exec(select(output_model)).all()

def read_object(session: Session, id: int, output_model: Type[OutputModel]) -> OutputModel:
    output_instance = session.get(output_model, id)
    if not output_instance:
        raise HTTPException(status_code=404, detail=f"{output_model.__name__} not found")
    return output_instance

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

def delete_object(session: Session, id: int, output_model: Type[OutputModel]) -> dict:
    output_instance = session.get(output_model, id)
    if not output_instance:
        raise HTTPException(status_code=404, detail=f"{output_model.__name__} not found")
    session.delete(output_instance)
    session.commit()
    return {"ok": True}
```
