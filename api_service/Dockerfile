FROM python:3.10

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app /app

WORKDIR /app

CMD ["python", "main.py"]