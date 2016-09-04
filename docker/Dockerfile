FROM ubuntu:xenial-20160809

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

ENV version 0.15

RUN apt-get update \
    && apt-get install -y \
       python3-pandas \
       python3-pip \
       python3-sqlalchemy \
       zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && pip3 install cython \
    && pip3 install bam_readgroup_to_json
