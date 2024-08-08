import os

def handle_uploaded_file(f):
    upload_dir = "uploads/"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, f.name)
    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
