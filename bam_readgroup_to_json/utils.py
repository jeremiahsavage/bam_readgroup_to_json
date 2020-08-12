#!/usr/bin/env python3

from types import SimpleNamespace

import pysam

DI = SimpleNamespace(pysam=pysam,)


def check_readgroup(readgroup_keys: List[str]):
    if not 'CN' in readgroup_dict:
        logger.info('"CN" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'ID' in readgroup_dict:
        logger.info('"ID" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'LB' in readgroup_dict:
        logger.info('"LB" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'PL' in readgroup_dict:
        logger.info('"PL" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'PU' in readgroup_dict:
        logger.info('"PU" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'SM' in readgroup_dict:
        logger.info('"SM" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    # if not 'DT' in readgroup_dict
    return


def legacy_check_readgroup(readgroup_dict):
    if not 'CN' in readgroup_dict:
        logger.info('"CN" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'ID' in readgroup_dict:
        logger.info('"ID" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'LB' in readgroup_dict:
        logger.info('"LB" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'PL' in readgroup_dict:
        logger.info('"PL" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'SM' in readgroup_dict:
        logger.info('"SM" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    # if not 'DT' in readgroup_dict
    return


def get_bam_header(bam_path: str, _di=DI) -> dict:
    """Use pysam to get bam header."""
    samfile = _di.pysam.AlignmentFile(bam_path, 'rb', check_sq=False)
    header = samfile.header
    return header
