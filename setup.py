#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = 'bam_readgroup_to_json',
      author = 'Jeremiah H. Savage',
      author_email = 'jeremiahsavage@gmail.com',
      version = 0.5,
      description = 'convert each readgroup id to a json file from a BAM',
      url = 'https://github.com/jeremiahsavage/bam_readgroup_to_json/',
      license = 'Apache 2.0',
      packages = find_packages(),
      install_requires = [
          'cython',
          'pandas',
          'pysam',
          'sqlalchemy',
          'cdis_pipe_utils'
      ],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
)
