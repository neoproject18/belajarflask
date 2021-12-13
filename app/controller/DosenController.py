from flask.json import jsonify
from sqlalchemy.orm import query
from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request
import math

# Menampilkan Semua Data Dosen


def index():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "Data dosen ditemukan!")

    except Exception as e:
        print(e)

def formatArray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id': data.id,
        'nidn': data.nidn,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat
    }
    return data

# Menampilkan Detail Dosen
def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter(
            (Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))
        if not dosen:
            return response.badRequest([], "Tidak ada data dosen!")

        dataMahasiswa = formatArrayMahasiswa(mahasiswa)
        data = singleDetailMahasiswa(dosen, dataMahasiswa)
        return response.success(data, "Data dosen ditemukan!")

    except Exception as e:
        print(e)

def formatArrayMahasiswa(datas):
    array = []
    for i in datas:
        array.append(singleObjectMahasiswa(i))

    return array

def singleObjectMahasiswa(data):
    data = {
        'id': data.id,
        'nim': data.nim,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat
    }
    return data

def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.nama,
        'phone': dosen.phone,
        'alamat': dosen.alamat,
        'mahasiswa': mahasiswa
    }
    return data

# Insert Data
def save():
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')
        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()

        return response.success('', 'Data dosen berhasil ditambahkan')
    except Exception as e:
        print(e)

# Update Data
def update(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                'nidn': nidn,
                'nama': nama,
                'phone': phone,
                'alamat': alamat
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()
        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat
        db.session.commit()

        return response.success(input, 'Data dosen berhasil diperbarui')
    except Exception as e:
        print(e)

# Hapus Data
def delete(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], 'Data dosen tidak ditemukan!')
        db.session.delete(dosen)
        db.session.commit()
        return response.success('', 'Dosen berhasil dihapus!')
    except Exception as e:
        print(e)

def getPagination(clss, url, start, limit):
    result = clss.query.all()
    data = formatArray(result)
    count = len(data)
    obj = {}

    if count < start:
        obj['success'] = False
        obj['message'] = "Page yang dipilih melewati batas total data!"
        return obj
    else:
        obj['success'] = True
        obj['start_page'] = start
        obj['per_page'] = limit
        obj['count'] = count
        obj['total_page'] = math.ceil(count/limit)

        #  Previous Link
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start-limit)
            limit_copy = start - 1
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)

        #  Next Link
        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)

        obj['result'] = data[(start - 1) : (start - 1 + limit)]

        return obj

# Pagging
def paginate():
    # Mengambil parameter get
    start = request.args.get('start')
    limit = request.args.get('limit')
    
    try:
        if start == None or limit == None:
            return jsonify(getPagination(
                Dosen,
                'http://127.0.0.1:5000/api/dosen/page',
                start = request.args.get('start', 1),                
                limit = request.args.get('limit', 3)
            ))
        else:
            return jsonify(getPagination(
                Dosen,
                'http://127.0.0.1:5000/api/dosen/page',
                start = int(start),                
                limit = int(limit)
            ))
    except Exception as e:
        print(e)