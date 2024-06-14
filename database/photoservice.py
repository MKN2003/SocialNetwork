from database import get_db
from database.models import PostPhoto
from datetime import datetime


# Загрузка изображений для посто
def add_photo_db(post_id, photo_path):
    db = next(get_db())
    photo = PostPhoto(post_id=post_id, photo_path=photo_path, red_data=datetime.now())
    db.add(photo)
    db.commit()
    return f'Успешно добавлено для этого {post_id}'


def get_all_photos():
    db = next(get_db())
    all_photos = db.query(PostPhoto).all()
    return all_photos