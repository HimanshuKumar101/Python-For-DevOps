import subprocess

def terraform_run(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(process.stdout.decode())

# Ensure the directory path is a raw string
directory = r"C:\Users\himan\OneDrive\Desktop\Python\terra-automate"
command = f"terraform -chdir={directory} init"

terraform_run(command)