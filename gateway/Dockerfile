FROM ubuntu:latest

# Set a directory for the app
WORKDIR /app

# Copy all the files from the host folder to the container
COPY . .

# Update apt-get repository  
RUN apt-get update -y

# Install Python, virtual environment support, and setuptools
RUN apt-get install python3 python3-venv python3-pip python3-setuptools -y

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment and install requirements
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r requirements.txt

EXPOSE 5050

# Run the app when the container launches
CMD ["python3", "./gateway.py"]