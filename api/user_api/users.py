from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.userservice import *
from datetime import datetime
from typing import Optional
from database import get_db
from database.models import User


class UserValidator(BaseModel):
    name: str
    phone_number: str
    email: str
    password: str
    birthday: Optional[str] = None
    user_city: Optional[str] = None
    status: Optional[str] = None


user_router = APIRouter(tags=['Управления пользователями'], prefix='/users')


# Регистрация
@user_router.post('/api/registration')
async def register_user(validator: UserValidator):
    db = next(get_db())
    user_data = validator.dict()
    user_email = user_data.get('email')
    print(user_email)
    checker = db.query(User).filter_by(email=user_email).first()
    print(f'ошибкаЖ {checker}')
    if not checker:
        try:
            reg_user = register_user_db(**user_data)
            return {'status': 1, "message": reg_user}
        except Exception as e:
            return {'status': 0, 'message': str(e)}
    else:
        return {'status': 0, 'message': 'Invalid email'}


# Логин пользователя
@user_router.post('/api/login')
async def login_user(email, password):
    user = login_db(email=email, password=password)
    return user


@user_router.get('/api/user')
async def get_user(user_id: int):
    exact_user = get_profile_db(user_id)
    return exact_user


@user_router.put('/api/change_account')
async def change_user_profile(id: int, change_info: str, new_info: str):
    data = change_user_data_db(id=id, change_info=change_info, new_info=new_info)
    return data


@user_router.get('/all-users')
async def all_user():
    db = next(get_db())
    users = db.query(User).all()
    return users


@user_router.delete('/api/delete_user')
async def delete_user(id: int):
    db = next(get_db())
    user_delete = delete_user_db(id=id)
    return user_delete
