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

WORKDIR '/finding-a-point'

RUN git init && \
    # git checkout -b develop && \
    git remote add origin https://c1cabe97056d6f0fd36f0ae90f3681ed9c650e11:x-oauth-basic@github.com/marewi/finding_a_point.git && \
    # git clone -b develop https://c1cabe97056d6f0fd36f0ae90f3681ed9c650e11:x-oauth-basic@github.com/marewi/finding_a_point.git /finding-a-point && \
    git pull origin develop

LABEL maintainer="marc-wittlinger@gmx.de"