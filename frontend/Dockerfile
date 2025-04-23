FROM python:latest


WORKDIR /app

COPY . .


COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# RUN pip install Flask
# RUN pip install flask_sqlalchemy
# RUN pip install flask_marshmallow
# RUN pip install marshmallow

EXPOSE 6050

CMD [ "python3", "./frontend.py" ]