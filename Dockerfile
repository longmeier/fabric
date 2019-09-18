FROM python:3.7-slim
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /src
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install -r requirements.txt
COPY . /src/
