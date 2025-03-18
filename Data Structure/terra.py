import subprocess

def terraform_init(command):
    subprocess.run(command, shell=True, check=True, text=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    