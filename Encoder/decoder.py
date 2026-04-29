import os
import py7zr
def decrypt_and_extract(archive_path, key_file_path, output_dir):
    with open(key_file_path, "r", encoding="utf-8") as f:
        content = f.read()
        password = content.split(": ")[1].strip()

    with py7zr.SevenZipFile(archive_path, mode = "r", password=password) as archive:
        archive.extractall(path=output_dir)

