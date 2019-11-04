#FROM node:6.9.2
FROM python:3.7

EXPOSE 80

#COPY server.js .

RUN git clone https://github.com/jhryu-zum/gcp-container-starer.git /workspace
#ENV APP_HOME /app
WORKDIR /workspace
RUN pip install requests zmq simplejson

#CMD node server.js
CMD python startproc.py
