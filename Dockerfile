FROM python:3.8-alpine3.11

WORKDIR /url-checker

COPY . /url-checker/
RUN pip3 install -r requirements.txt

#RUN python3 main.py