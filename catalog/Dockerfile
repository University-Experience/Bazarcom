FROM python:3.10

# set a directory for the app
WORKDIR /app

COPY . .

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# Run client.py when the container launches
CMD ["python3", "./catalog.py"]