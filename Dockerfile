FROM ubuntu:bionic-20180426

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

ENV version 0.26

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
        cython \
        libbz2-1.0 \
        libbz2-dev \
        liblzma5 \
        liblzma-dev \
        make \
        python3-pandas \
        python3-pip \
        python3-sqlalchemy \
        zlib1g \
        zlib1g-dev \
    && apt-get clean \
    && pip3 install bam_readgroup_to_json \
    && apt-get remove --purge -y \
        cython \
        libbz2-dev \
        liblzma-dev \
        make \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache
