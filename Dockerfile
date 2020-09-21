FROM ubuntu:latest

MAINTAINER arif.darmawan@riflab.com 

RUN apt-get update \
	&& apt-get install -y python3 python3-pip \
	&& pip3 install instapy \
	&& apt-get install -y vim \ 
	# && sudo apt-get install -y firefox

COPY quickstart.py /.





