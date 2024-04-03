FROM python:3.10.14-alpine

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system --deploy

COPY ./app /app/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
