# Use the official Python slim image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files into the container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that Streamlit will use
EXPOSE 8501

# Run the Streamlit app, using main.py as the entry point
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
