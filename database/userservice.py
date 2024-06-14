from database.models import User
from database import get_db
from datetime import datetime
# from jose import JWTError, jwt
# from datetime import timedelta
#
# from main import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


# def create_access_token(data: dict):
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     data.update({'exp': expire})
#     encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
#
#     return encoded_jwt


# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except JWTError:
#         return None


# Проверка данных пользователя
def check_user_db(name, email, phone_number):
    db = next(get_db())
    checker_name = db.query(User).filter_by(name=name).first()
    checker_email = db.query(User).filter_by(email=email).first()
    checker_phone_number = db.query(User).filter_by(phone_number=phone_number).first()
    if checker_name:
        return "Такой Username уже занят"
    elif checker_email:
        return "Такой email уже занят"
    elif checker_phone_number:
        return "Такой номер уже занят"
    else:
        return True


# Регистрация пользовтеля
def register_user_db(name, email, phone_number, password, user_city=None, birthday=None, status=None):
    db = next(get_db())
    checker = check_user_db(name, email, phone_number)
    if checker:
        new_user = User(name=name, email=email, phone_number=phone_number, password=password, birthday=birthday,
                        user_city=user_city, status=status, reg_date=datetime.now())
        db.add(new_user)
        db.commit()
        return f'Регистрация пользователя {new_user.id} проведена успешна'
    else:
        checker


# Логин
def login_db(email, password):
    db = next(get_db())
    user_email = db.query(User).filter_by(email=email).first()
    # user_password = db.query(User).filter_by(password=password).first()
    print(user_email)
    if user_email:
        if user_email.password == password:
            return user_email
        else:
            return "Неправильные данные"
    else:
        return 'Нет такого email'


# Получение данных определенного пользователя
def get_profile_db(id):
    db = next(get_db())
    user_info = db.query(User).filter_by(id=id).first()
    if user_info:
        return user_info
    return False


# Изменения данных пользователя
def change_user_data_db(id, change_info, new_info):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        try:
            if change_info == 'name':
                user.name = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'email':
                user = db.query(User).filter_by(email=new_info).first()
                if user:
                    return 'Этот имейл уже занят'
                else:
                    user.email = new_info
                    db.commit()
                    return 'Успешно изменено'
            elif change_info == 'city':
                user.city = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'password':
                user.password = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'birthday':
                user.birthday = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'phone_number':
                user.phone_number = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'status':
                user.status = new_info
                db.commit()
                return 'Успешно изменено'
            else:
                return 'Таких данных не существует'
        except:
            return 'Нет такого значения для изменения'
    return False


# Удаление пользовтеля Logout
def delete_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        db.delete(user)
        db.commit()
        return 'Успешно удалено'
    return False

