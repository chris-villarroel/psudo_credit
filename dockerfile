# Use the official Python 3.10 Alpine image
FROM python:3.10-alpine

# Set working directory in container
WORKDIR /app

# Copy local folder into the container at /app
COPY . /app

# Since Alpine uses a different C library (musl) instead of glibc, 
# you might need to install some build dependencies depending on your requirements.txt.
# Here's an example of installing build-base which provides basic build tools.
RUN apk add --no-cache build-base && \
    . /app/venv/bin/activate && \
    pip install -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Command to run the application using python
CMD ["python", "app.py"]