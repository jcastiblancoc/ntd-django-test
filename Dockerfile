FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY django_crud/ /app/

# Create logs directory
RUN mkdir -p /app/logs

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
