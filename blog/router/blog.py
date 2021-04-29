from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas
from typing import List
from pydantic import BaseModel
from .. import schemas, models, database, oauth2
# from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.get('/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def show(id, response: Response,  db: Session = Depends(get_db)):
    return blog.show(id, response, db)


@router.put('/{id}')
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.destroy(id, db)
