import hashlib

def calculate_file_hash(filepath):
    with open(filepath, 'rb') as f:
        filehash = hashlib.md5(f.read()).hexdigest()
        return filehash



    