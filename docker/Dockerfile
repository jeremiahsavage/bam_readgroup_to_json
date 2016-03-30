FROM quay.io/jeremiahsavage/cdis_base

USER root

RUN apt-get update && apt-get install -y --force-yes \
    s3cmd

USER ubuntu

ENV bam_readgroup_to_json 0.1

RUN /bin/bash -c "source ${HOME}/.virtualenvs/p3/bin/activate \
    && pip install bam_readgroup_to_json"
