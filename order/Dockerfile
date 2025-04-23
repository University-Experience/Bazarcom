FROM ubuntu:22.04

WORKDIR /app
COPY . .

RUN apt-get update -y
RUN apt-get install python3.10 python3.10-venv python3.10-dev python3-pip python3-setuptools -y

RUN python3.10 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 6000
CMD ["python3", "./order.py"]