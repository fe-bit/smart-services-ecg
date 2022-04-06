# syntax=docker/dockerfile:1

#FROM python:3.7.13-alpine3.15
#FROM python:alpine3.15
FROM python:3.9.12-slim-buster
WORKDIR .

#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
RUN pip install tensorflow numpy flask
COPY . .

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["python3", "-m", "start_server"] 