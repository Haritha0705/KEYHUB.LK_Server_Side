FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY src /code/src
COPY alembic /code/alembic
COPY alembic.ini /code/alembic.ini

CMD ["sh", "-c", "alembic upgrade head && fastapi run src/app/main.py --port 8000"]