from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.userservice import *
from database.postservice import *
from database.photoservice import *
from datetime import datetime
from typing import Optional
from database import get_db
from database.models import User, UserPost

post_router = APIRouter(tags=['Управление постами'], prefix='/posts')


@post_router.get('/all-posts')
async def get_all_posts():
    db = next(get_db())
    posts = db.query(UserPost).all()
    return posts


@post_router.get('/api/post')
async def get_exact_post(id: int):
    exact_post = get_exact_post_db(id=id)
    return exact_post


@post_router.get('/all-photos')
async def get_all_photos():
    db = next(get_db())
    photos = db.query(PostPhoto).all()
    return photos


@post_router.post('/api/add-post')
async def add_post(user_id, main_text, description, hashtag=None):
    post_add = add_post_db(user_id=user_id, main_text=main_text, description=description, hashtag=hashtag)
    return post_add


@post_router.post('/api/add-comment')
async def add_comment(user_id, id, comment_text):
    comment_add = public_comment_db(user_id=user_id, id=id, comment_text=comment_text)
    return comment_add


@post_router.post('/api/add-hashtag')
async def add_hashtag(hashtag_name):
    hashtag_add = add_hashtag_db(hashtag_name=hashtag_name)
    return hashtag_add


@post_router.post('/api/add-photo')
async def add_photo(post_id, photo_path):
    photo = add_photo_db(post_id=post_id, photo_path=photo_path)
    return photo


@post_router.get('/api/get-comment')
async def get_exact_comment(id):
    comment = get_exact_post_comment_db(id=id)
    return comment


@post_router.get('/all-hashtag')
async def get_all_hashtag():
    db = next(get_db())
    hashtags = db.query(Hashtag).all()
    return hashtags


@post_router.get('/api/get-hashtag')
async def get_exact_hashtag(hashtag_name):
    hashtag = get_exact_hashtag_db(hashtag_name=hashtag_name)
    return hashtag


@post_router.get('/api/recommend-hashtag')
async def get_recommended_hashtag(hashtag_name, size):
    recommended_hashtag = get_recommend_hashtag_db(size=size, hashtag_name=hashtag_name)
    return recommended_hashtag


@post_router.put('/api/change-post')
async def change_post(id, new_text):
    post_change = change_post_db(id=id, new_text=new_text)
    return post_change


@post_router.put('/api/change-comment')
async def change_comment_text(id, new_text):
    comment_change = change_comment_text_db(id=id, new_text=new_text)
    return comment_change


@post_router.delete('/api/delete-post')
async def delete_post(id):
    post_delete = delete_post_db(id=id)
    return post_delete


@post_router.delete('/api/delete-comment')
async def delete_comment(id):
    comment_delete = delete_exact_comment_db(id=id)
    return comment_delete


@post_router.delete('/api/delete-hashtag')
async def delete_hashtag(hashtag_name):
    hashtag_delete = delete_hashtag_db(hashtag_name=hashtag_name)
    return hashtag_delete
