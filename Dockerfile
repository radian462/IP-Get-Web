FROM python:3.11
WORKDIR /web
RUN apt update
COPY requirements.txt /web/
RUN pip install -r requirements.txt
COPY . /web
CMD python main.py
