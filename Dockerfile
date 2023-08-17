FROM python:3.9-slim

LABEL maintainer="Prajwal Patil patilprajwal22@gmail.com"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]