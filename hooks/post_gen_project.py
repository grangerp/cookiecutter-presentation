import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if '{{ cookiecutter.use_docker }}'.lower() != 'y':
    for filename in ['docker-compose.yml', 'Dockerfile']:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))
