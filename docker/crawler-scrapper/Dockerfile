FROM ubuntu:18.04

RUN apt-get update

RUN apt-get -y install python3.6 &&\
    apt-get -y install python3-pip

RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

COPY /collector/requirements.txt /collector/requirements.txt

RUN pip3 install -r /collector/requirements.txt

COPY /collector /collector

WORKDIR /collector 


