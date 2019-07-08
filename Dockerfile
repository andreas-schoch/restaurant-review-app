FROM ubuntu:16.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt update && apt upgrade -y && apt install -qqy \
    wget \
    bzip2 \
    libssl-dev \
    openssh-server \
    nodejs \
    npm

RUN apt-get autoremove -y

### Start of SSH Setup ###
RUN mkdir /var/run/sshd
RUN echo "root:pinguinwings" | chpasswd
RUN sed -i "/PermitRootLogin/c\PermitRootLogin yes" /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed "s@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g" -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
### End of SSH Setup ###

# Install miniconda
RUN echo 'export PATH=/opt/miniconda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/miniconda && \
    rm ~/miniconda.sh

# NodeJS
RUN npm install -g n
RUN n 9.11.1

RUN mkdir -p /api && \
    mkdir -p /frontend | \
    mkdir -p /scripts && \
    mkdir -p /media-files && \
    mkdir -p /static-files

COPY ./api/requirements.yml /api/requirements.yml

RUN /opt/miniconda/bin/conda env create -f /api/requirements.yml

ENV PATH /opt/miniconda/envs/api/bin:$PATH
RUN sed '$ a source activate api' -i /root/.bashrc

WORKDIR /frontend
COPY ./frontend/package.json /frontend/
RUN npm install
COPY ./frontend /frontend
RUN npm run build

COPY ./api /api

COPY ./scripts /scripts
RUN chmod +x /scripts/*

WORKDIR /api

EXPOSE 8000
EXPOSE 22
