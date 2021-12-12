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
