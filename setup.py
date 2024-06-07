import subprocess

def launch_app(venv_path):
    try:
        #new && python manage.py collectstatic
        subprocess.run(
            f"source {venv_path}/bin/activate && python manage.py collectstatic && python manage.py makemigrations  && python manage.py migrate", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to activate virtual environment: {e}")

venv_path = "/home/kuazoneg/virtualenv/bayden/3.11"
launch_app(venv_path)



