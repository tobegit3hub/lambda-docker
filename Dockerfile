FROM ubuntu:15.04
MAINTAINER tobe tobeg3oogle@gmail.com

RUN apt-get update -y
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip

ADD . /usr/lib/
WORKDIR /usr/lib/lambda-docker

RUN pip install -r /usr/lib/lambda-docker/requirements.txt

CMD ['./server.py']
