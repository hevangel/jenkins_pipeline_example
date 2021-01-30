# base image
FROM python

# Example Dockerfile
MAINTAINER jenkins@hevangel.com
LABEL "com.example.vendor"="hevangel.com"
LABEL version=1.0
LABEL description="Example Dockerfile"

# install python
COPY requirements.txt /home
RUN pip3 install --no-cache-dir -r /home/requirements.txt

# external mount point 
VOLUME /work

# set work directory
WORKDIR /work

ARG CALLER='Jenkins'
ENTRYPOINT echo "Welcome $CALLER"
