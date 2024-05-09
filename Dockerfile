FROM python:3.8-alpine

WORKDIR /bot

COPY requirements.txt .

RUN pip install --no-cache-dir -r /bot/requirements.txt

COPY . .

WORKDIR /bot

CMD ["python3", "main.py"]
