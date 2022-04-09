FROM python:3.10.4-alpine3.15

ENV WORKSPACE /home/project

WORKDIR /home/project
COPY requirements.txt /home/project

RUN python3 -m venv venv
RUN source venv/bin/activate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
