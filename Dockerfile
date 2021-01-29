# base image
FROM ubuntu:20.04

# Example Dockerfile
MAINTAINER jenkins@hevangel.com
LABEL "com.example.vendor"="hevangel.com"
LABEL version=1.0
LABEL description="Example Dockerfile"

# install python
RUN apt update
RUN apt install -y python3 python3-pip
COPY requirements.txt /home
RUN pip3 install -r /home/requirements.txt

# external mount point 
VOLUME /work

# set work directory
WORKDIR /work

ARG CALLER='Jenkins'
ENTRYPOINT echo "Welcome $CALLER"
