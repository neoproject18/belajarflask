ALLOWED_EXTENTION = set(['png','jpg','jpeg','pdf'])

def get_ext(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTION