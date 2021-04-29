from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} blog list'}
    else:
        return {'data': 'All blog list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}


@app.get('/blog/{id}')
# fetch blog with id
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
# fetch comments of blog with id
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return{'data': f'blog created with {blog.title}'}
