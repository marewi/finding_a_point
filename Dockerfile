FROM tensorflow/tensorflow:latest-py3
# #FROM tensorflow/tensorflow-gpu

RUN apt-get update && \
    apt-get install -y libsm6 libxext6 libxrender-dev && \
    apt-get install -y git

RUN pip install --upgrade pip && \
    pip install Pillow && \
    pip install opencv-python && \
    pip install matplotlib && \
    pip install xlrd && \
    pip install prettytable

RUN mkdir /developer

# # import lib
# ADD ./lib /developer

WORKDIR '/developer'

LABEL maintainer="marc-wittlinger@gmx.de"