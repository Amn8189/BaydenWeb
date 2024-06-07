import subprocess

def launch_app():
    try:
        subprocess.run(
            f"source {venv_path}/bin/activate && python manage.py makemigrations && python manage.py migrate", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to activate virtual environment: {e}")

venv_path = ""
launch_app(venv_path)



