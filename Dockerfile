# Use official Python image matching runtime.txt
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Arguments needed at build-time, to be provided by Coolify
ARG DATABASE_URL

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

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port (default for Gunicorn)
EXPOSE 8001

# Run migrations and start server
CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8001"]