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

# Expose the port used by Streamlit
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

