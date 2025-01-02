FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${FLASK_PORT}

CMD ["python", "app.py"]