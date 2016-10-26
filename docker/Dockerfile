FROM ubuntu:xenial-20161010

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

ENV version 0.17

RUN apt-get update \
    && apt-get install -y \
       python3-pandas \
       python3-pip \
       python3-sqlalchemy \
       zlib1g-dev \
    && apt-get clean \
    && pip3 install cython \
    && pip3 install bam_readgroup_to_json \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*