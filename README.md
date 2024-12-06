# pyaudit-decorator
A Python decorator for auditing user activity

## Setup and run locally

Create and set the virtual environment

    pyenv virtualenv 3.12.2 pyaudit-decorator-3.12.2
    pyenv local pyaudit-decorator-3.12.2

    pip3 install -r requirements.txt

## Run tests

    pytest

## Local development

Install linting tools into the virtual environment:

    python3 -m pip install flake8
    python3 -m pip install black
    python3 -m pip install isort
