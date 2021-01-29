# Example Dockerfile
MAINTAINER jenkins@hevangel.com
LABEL "com.example.vendor"="hevangel.com"
LABEL version=1.0
LABEL description="Example Dockerfile"

# base image
FROM ubuntu:20.04

# install python
RUN apt install python3 python3-pip
COPY requirements.txt /work
RUN pip3 install -r /work/requirments.txt

# external mount point 
VOLUME /work

# set work directory
WORKDIR /work

ARG CALLER='Jenkins'
ENTRYPOINT echo "Welcome $CALLER"
