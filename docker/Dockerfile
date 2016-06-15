FROM quay.io/jeremiahsavage/cdis_base

USER ubuntu

ENV bam_readgroup_to_json 0.7

RUN /bin/bash -c "source ${HOME}/.virtualenvs/p3/bin/activate \
    && pip install bam_readgroup_to_json"
