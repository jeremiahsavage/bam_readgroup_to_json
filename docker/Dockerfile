FROM quay.io/jeremiahsavage/cdis_base

USER ubuntu

ENV bam_readgroup_to_json 0.8

RUN /bin/bash -c "source ${HOME}/.virtualenvs/p3/bin/activate \
    && pip install bam_readgroup_to_json"
