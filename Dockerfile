FROM python:3.8.10

RUN mkdir /app_grupo6
WORKDIR /app_grupo6

RUN pip install --upgrade pip

COPY requirements.txt /app_grupo6/

RUN pip install -r requirements.txt

COPY . /app_grupo6/

RUN mkdir /app_grupo6/data

ENV RUNNING_IN_DOCKER = True

CMD [ "python", "NotiBarrio/manage.py", "runserver", "0.0.0.0:8000"]