FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install django
RUN pip install psycopg2
RUN pip install django-allauth
WORKDIR /src
COPY ./src/* /src