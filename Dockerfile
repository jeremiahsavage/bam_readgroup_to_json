FROM python:3.6-stretch

MAINTAINER Charles Czysz <czysz@uchicago.edu>

ENV BINARY=bam_readgroup_to_json

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
        cython \
        libbz2-1.0 \
        libbz2-dev \
        liblzma5 \
        liblzma-dev \
        zlib1g \
        zlib1g-dev

COPY ./dist/ /opt

WORKDIR /opt

RUN make init-pip
	# && ln -s /opt/bin/${BINARY} /usr/local/bin/${BINARY}

RUN apt-get remove --purge -y \
        cython \
        libbz2-dev \
        liblzma-dev \
        make \
        zlib1g-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache

ENTRYPOINT ["bam_readgroup_to_json"]

CMD ["--help"]
