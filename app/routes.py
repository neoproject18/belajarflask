from flask_migrate import current
from werkzeug.wrappers import request
from app import app, response
from app.controller import DosenController, UserController
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required


@app.route('/')
def index():
    return 'Hello Flask App'


# @app.route('/createadmin', methods=['POST'])
# def admins():
#     return UserController.createAdmin()

@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, "Sukses")

@app.route('/dosen', methods=['GET', 'POST'])
@jwt_required()
def dosens():
    if request.method == 'GET':
        return DosenController.index()
    else:
        return DosenController.save()

# Route Pagination
@app.route('/api/dosen/page', methods=['GET'])
@jwt_required()
def pagination():
    return DosenController.paginate()


@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def dosensDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.update(id)
    else:
        return DosenController.delete(id)

@app.route('/file-upload', methods=['POST'])
# @jwt_required()
def uploads():
    return UserController.upload()
