from database import get_db
from .models import UserPost, Comment, Hashtag, PostPhoto
from datetime import datetime


# Получить все посты
def get_all_posts():
    db = next(get_db())
    posts = db.query(UserPost).all()
    return posts


# Получить определенный пост
def get_exact_post_db(id: int):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=id).first()
    if exact_post:
        return exact_post
    return 'Нет такого поста'


# Изменить определнный пост
def change_post_db(id, new_text):
    db = next(get_db())
    post_to_edit = db.query(UserPost).filter_by(id=id).first()
    if post_to_edit:
        post_to_edit.main_text = new_text
        db.commit()
        return 'Усешно изменено'
    return False


# Удалить определенный пост
def delete_post_db(id):
    db = next(get_db())
    post_to_delete = db.query(UserPost).filter_by(id=id).first()
    if post_to_delete:
        db.delete(post_to_delete)
        db.commit()
        return 'Пост успешно удален'
    return "Нет такого поста"


# Добавления поста
def add_post_db(user_id, main_text, description, hashtag=None):
    db = next(get_db())
    if user_id:
        new_post = UserPost(user_id=user_id, main_text=main_text, description=description,
                            reg_date=datetime.now(), hashtag=hashtag)
        db.add(new_post)
        db.commit()
        return 'Пост успешно добавлен'
    return 'Такого пользователя нет'


# Добавлеия комментраиев
def public_comment_db(user_id, id, comment_text):
    db = next(get_db())
    if user_id and id:
        new_comment = Comment(user_id=user_id, id=id, comment_text=comment_text)
        db.add(new_comment)
        db.commit()
        return 'Коментарий успешно добавлен'
    return 'Нет такого поста либо пользователя'


# Получить комментрии определенного поста
def get_exact_post_comment_db(id):
    db = next(get_db())
    exact_comments = db.query(Comment).filter_by(id=id).all()
    if exact_comments:
        return exact_comments
    return False


# Изменить текст коментария
def change_comment_text_db(id, new_text):
    db = next(get_db())
    comment_edit = db.query(Comment).filter_by(id=id).first()
    if comment_edit:
        comment_edit.comment_text = new_text
        db.commit()
        return 'Успешно изменен'
    return False


# Удаления определенного комментраия
def delete_exact_comment_db(id):
    db = next(get_db())
    comment_delete = db.query(Comment).filter_by(id=id).first()
    if comment_delete:
        db.delete(comment_delete)
        db.commit()
        return 'Коментарии успешно удален'
    return False


# Создание хэштега
def add_hashtag_db(hashtag_name):
    db = next(get_db())
    new_hashtag = Hashtag(hastag_name=hashtag_name, reg_data=datetime.now())
    db.add(new_hashtag)
    db.add.commit()
    return True


# Рекомендации по хэштегу
def get_recommend_hashtag_db(size, hashtag_name):
    db = next(get_db())
    posts = db.query(UserPost).filter_by(hashtag_name=hashtag_name).limit(size).all()
    return posts


# Получить определенный хэштег
def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())
    exact_hashtag = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()
    if exact_hashtag:
        return exact_hashtag
    return False


# Получить все хэштешги
def get_all_hashtag_db():
    db = next(get_db())
    hashtags = db.query(Hashtag).all()
    return hashtags


# Удалить определенный хэштега
def delete_hashtag_db(hashtag_name):
    db = next(get_db())
    hashtag_to_delete = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()
    if hashtag_to_delete:
        db.delete(hashtag_to_delete)
        db.commit()
        return "Хэштег был успешно удален"
    return False