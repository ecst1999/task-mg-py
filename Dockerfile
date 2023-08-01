FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requeriments.txt requeriments.txt
RUN pip3 install -r requeriments.txt
COPY . .

WORKDIR /app/taskmg
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]