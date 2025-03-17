import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_files_name = os.path.join(destination, f"backup_{today}")  # No .tar.gz here
    shutil.make_archive(backup_files_name.replace('.tar.gz',''), 'gztar', source)

# Use raw strings (r"") or double backslashes (\\) to fix path errors
source = r"C:\Users\himan\OneDrive\Desktop\Python\DevOps"
destination = r"C:\Users\himan\OneDrive\Desktop\Python\DevOps\Backup"

backup_files(source, destination)

print("Backup completed successfully!")
