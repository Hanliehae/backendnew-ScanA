from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Autentikasi
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Hanya pertama kali, buka browser untuk autentikasi
drive = GoogleDrive(gauth)

def upload_file_to_drive(local_path, drive_folder_id):
    file_name = os.path.basename(local_path)
    gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': drive_folder_id}]})
    gfile.SetContentFile(local_path)
    gfile.Upload()
    print(f"Uploaded {file_name} to Google Drive folder ID: {drive_folder_id}")

def upload_folder_to_drive(local_folder_path, drive_folder_id):
    for filename in os.listdir(local_folder_path):
        file_path = os.path.join(local_folder_path, filename)
        if os.path.isfile(file_path):
            upload_file_to_drive(file_path, drive_folder_id)