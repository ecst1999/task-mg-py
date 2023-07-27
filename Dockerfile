FROM python:3.12.0b4-alpine as builder
WORKDIR /app
COPY requeriments.txt requeriments.txt
RUN pip3 install -r requeriments.txt
COPY . .

FROM python:3.12.0b4-alpine as data
COPY --from=builder /app /app
WORKDIR /app/taskmg
RUN python3 manage.py makemigrations && python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

