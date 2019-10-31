FROM tensorflow/tensorflow:latest-py3
# #FROM tensorflow/tensorflow-gpu

RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get install -y git

RUN pip install --upgrade pip

RUN pip install Pillow
RUN pip install opencv-python
RUN pip install matplotlib
RUN pip install xlrd
RUN pip install prettytable

# ADD . /developer

# # import lib
# ADD ./lib /developer

WORKDIR '/developer'

LABEL maintainer="marc-wittlinger@gmx.de"