# This dockerfile uses the ubuntu image
# Version 1
# Author : Kenny Hsieh

FROM ubuntu:14.04
MAINTAINER Kenny Hsieh – kenny037286@gmail.com

RUN apt-get update \
    && apt-get -y upgrade \ 
    && apt-get -y install build-essential gcc make git wget net-tools \
    && apt-get install -y python3-pip \
    && pip3 install flask flask-uploads
RUN cd opt \
    && git clone https://github.com/kennyhsieh1111/Dockerize-YOLO-Service.git \
    && cd Dockerize-YOLO-Service \
    && rm -rf darknet
RUN cd opt/Dockerize-YOLO-Service \
    && git clone https://github.com/pjreddie/darknet.git \
    && mv image.c darknet/src \
    && mv prediction_label.txt darknet
RUN cd opt/Dockerize-YOLO-Service/darknet \ 
    && wget https://pjreddie.com/media/files/yolov3.weights \ 
    && make

WORKDIR opt/Dockerize-YOLO-Service
EXPOSE 5000
CMD ["python3", "app.py"]

