from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas
from typing import List
from pydantic import BaseModel
from .. import schemas, models, database
# from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=["User"]
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_user(id, db)
