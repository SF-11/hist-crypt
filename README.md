# hist-crypt
Historical Cryptography

## Setup Virtual Environment
pip install virtualenv
python3 -m venv venv
source venv/bin/activate (or: venv\Scripts\activate)
pip install -r requirements.txt

## Run Tests
python -m pytest --cov-report term-missing --cov