FROM python:3.8

WORKDIR /app
ADD . /app/

RUN pip install -r ./requirements.txt
# RUN python ./manage.py makemigrations
# RUN python ./manage.py migrate
# RUN python ./manage.py runserver

