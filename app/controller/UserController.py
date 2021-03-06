import datetime
from app.model.user import User
from app.model.galeri import Galeri
import os
from app import response, app, db, uploadconfig
import uuid
from werkzeug.utils import secure_filename

from flask import request
from flask_jwt_extended import *


# def createAdmin():
#     try:
#         name = request.form.get('name')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         level = 1

#         users = User(name=name, email=email, level=level)
#         users.setPassword(password)
#         db.session.add(users)
#         db.session.commit()

#         return response.success('', 'Berhasil membuat admin!')
#     except Exception as e:
#         print(e)

def singleObject(data):
    return {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "level": data.level,
    }

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], "Email tidak terdaftar!")
        
        if not user.checkPassword(password):
            return response.badRequest([], "Password salah!")
        
        data = singleObject(user)
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)
        access_token = create_access_token(data, fresh = True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        print(data)

        return response.success({
            "data": data,
            "access_token": access_token,
            "refresh_token": refresh_token
        }, "Login berhasil")

    except Exception as e:
        print(e)

def upload():
    try:
        filename = request.form.get('filename')
        if 'file' not in request.files:
            return response.badRequest([],'File tidak tersedia')
        
        file = request.files['file']
        if file.filename == '':
            return response.badRequest([],'File tidak tersedia')
        
        if file and uploadconfig.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = "Flask-" + str(uid) + filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], renamefile)
            file.save(path)
            file_length = os.stat(path).st_size

            upload = Galeri(filename=filename, size=file_length, type=uploadconfig.get_ext(file.filename), pathname = renamefile)
            db.session.add(upload)
            db.session.commit()
            return response.success({
                'filename': filename,
                'pathname': renamefile
            }, 'Upload file galeri berhasil!')
        else:
            return response.badRequest([],'File tidak diizinkan')

    except Exception as e:
            print(e)