FROM python:3.7-slim

RUN mkdir /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /app

#CMD ["python3", "manage.py", "runserver", "0:8000"]

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8084"]

