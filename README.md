# Membuat project
mkdir [nama folder]
cd [nama folder]

# Membuat Environment
virtualenv env

# Mengaktifkan environment
env\Scripts\activate.bat

# Mengnonaktifkan environment
deactivate

# Menginstal Flask di Environment
pip install flask 
pip install python-dotenv

# Menjalankan server
flask run

# Installasi agar dapat membuat tabel dari flask
pip install flask-sqlalchemy
pip install flask-migrate

# Install to Connect MySQL
pip install pymysql

# Inisialisasi Database
flask db init

# Migrasi Database
flask db migrate -m "isi komentar"

# Upgrade Database
flask db upgrade

# Merge Database
flask db stamp head
flask db merge heads -m "merging two heads"

# Install JWT
pip install flask-jwt-extended

# Install Password Hash
pip install werkzeug