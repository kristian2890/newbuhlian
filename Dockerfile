# Use official Python image matching runtime.txt
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Make sure manage.py is in /app
RUN ls -l /app/manage.py

RUN python manage.py help

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port (default for Gunicorn)
EXPOSE 8000

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && gunicorn blog.wsgi:application --bind 0.0.0.0:8000 --log-file -"]