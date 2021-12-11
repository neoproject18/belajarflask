from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

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
