# Step 1: Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set the working directory
WORKDIR /app

# Step 4: Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Step 6: Copy the Django project files to the working directory
COPY . /app/

# Step 7: Expose the port on which the app will run
EXPOSE 8000

# Step 8: Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
