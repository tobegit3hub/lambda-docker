FROM ubuntu:15.04
MAINTAINER tobe tobeg3oogle@gmail.com

RUN apt-get update -y
RUN apt-get install -y python-dev python-pip

RUN mkdir /usr/lib/lambda-docker
WORKDIR /usr/lib/lambda-docker

ADD requirements.txt /usr/lib/lambda-docker/requirements.txt
RUN pip install -r /usr/lib/lambda-docker/requirements.txt

ADD . /usr/lib/lambda-docker

CMD /usr/lib/lambda-docker/server.py

