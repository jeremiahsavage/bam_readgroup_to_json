#!/usr/bin/env python
"""Outputs readgroup header, as JSON, from given BAM.
"""

import argparse
import collections
import json
import logging
import os
import sys
from types import SimpleNamespace

import pysam

from bam_readgroup_to_json import extract, legacy, utils

logger = logging.getLogger(__name__)


def setup_logger(args):
    logging.basicConfig(
        filename=args.log_file,
        level=args.log_level,
        filemode='w',
        format='%(asctime)s %(name)s:%(lineno)s %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S_%Z',
    )


DI = SimpleNamespace(json=json, open=open, os=os, pysam=pysam,)

READGROUP_REQUIRES = (
    'CN',
    'ID',
    'LB',
    'PL',
    'PU',
    'SM',
)
LEGACY_READGROUP_REQUIRES = (
    'CN',
    'ID',
    'LB',
    'PL',
    'SM',
)


def setup_logging(level=logging.INFO):
    logging.basicConfig(
        filename=os.path.join('output.log'),
        level=level,
        filemode='w',
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S_%Z',
    )
    logger = logging.getLogger(__name__)
    return logger


def parse_args(argv=None):

    parser = setup_parser()
    if argv:
        args, unknown_args = parser.parse_known_args(argv)
    else:
        args, unknown_args = parser.parse_known_args()

    args_dict = vars(args)

    args_dict['extras'] = unknown_args

    run_args = collections.namedtuple('RunArgs', list(args_dict.keys()))
    return run_args(**args_dict)


def setup_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser('convert readgroups to json')

    # Logging flags.
    parser.add_argument(
        '-d',
        '--debug',
        action='store_const',
        const=logging.DEBUG,
        dest='level',
        help='Enable debug logging.',
    )
    parser.set_defaults(level=logging.INFO)

    # Required flags.
    parser.add_argument('-b', '--bam-path', required=True, help='BAM file.')
    parser.add_argument(
        '-m', '--mode', required=True, choices=('strict', 'lenient'),
    )
    return parser


def run(args):

    mode = args.mode
    bam_path = args.bam_path

    if mode == 'strict':
        extract.extract_readgroup_json(bam_path)
    elif mode == 'lenient':
        legacy.extract_readgroup_json(bam_path)

    return


def main() -> int:
    retcode = 0
    parser = argparse.ArgumentParser('convert readgroups to json')

    # Logging flags.
    parser.add_argument(
        '-d',
        '--debug',
        action='store_const',
        const=logging.DEBUG,
        dest='level',
        help='Enable debug logging.',
    )
    parser.set_defaults(level=logging.INFO)

    # Required flags.
    parser.add_argument('-b', '--bam-path', required=True, help='BAM file.')
    parser.add_argument(
        '-m', '--mode', required=True, choices=('strict', 'lenient'),
    )

    args = parser.parse_args()

    try:
        run(args)
    except Exception as e:
        logger.exception(e)
        retcode = 1
    return retcode


if __name__ == '__main__':

    exit_code = 0
    try:
        exit_code = main()
    except Exception as e:
        logger.exception(e)
        exit_code = 1
    sys.exit(exit_code)
