import py7zr   
import os
import shutil
from datetime import datetime
def create_protected_archive(target_path, password):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    archive_dir = os.path.join(base_dir, "archives") 
    key_dir = os.path.join(base_dir, "passwords")

    os.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    folder_name = os.path.basename(target_path)
    archive_name = f"{folder_name}_{os.timestamp}.7z"

    full_archive_path = os.path.join(archive_dir, archive_name)
    full_key_path = os.path.join(key_dir, f"key_{archive_name}.txt")

    with py7zr.SevenZipFile(full_archive_path, 'w', password=password) as archive:
        archive.writeall(target_path, folder_name)
    with open(full_key_path, "w", encoding="utf-8") as f:
        f.write(f"Пароль для архива {archive_name}: {password}")
    shutil.rmtree(target_path)

    return full_archive_path, full_key_path