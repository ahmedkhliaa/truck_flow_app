# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY . .

# Install system dependencies for psycopg2 (and any other packages that need building)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ✅ Change exposed port to 8080 (Cloud Run requirement)
EXPOSE 8080

# ✅ Change Streamlit to listen on port 8080 (Cloud Run talks only to 8080)
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]


