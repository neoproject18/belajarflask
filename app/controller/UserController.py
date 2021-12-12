from app.model.user import User

from app import response, app, db
from flask import request


def createAdmin():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        users = User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', 'Berhasil membuat admin!')
    except Exception as e:
        print(e)
