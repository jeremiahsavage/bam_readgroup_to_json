#!/usr/bin/env python3

import json
from types import SimpleNamespace
from typing import List

from bam_readgroup_to_json import utils

DI = SimpleNamespace(json=json, open=open,)


READGROUP_REQUIRES = (
    'CN',
    'ID',
    'LB',
    'PL',
    'PU',
    'SM',
)


def check_readgroup(
    readgroup_keys: List[str], required_keys: list = READGROUP_REQUIRES
) -> list:
    missing_keys = [x for x in readgroup_keys if x not in required_keys]
    return missing_keys


def extract_readgroup_json(bam_path: str, _utils=utils, _di=DI):
    """Reads readgroup header from given BAM.

    Raises:
        ValueError: No readgroup info.
    """

    bamfile_header = _utils.get_bam_header(bam_path)
    readgroup_dict_list = bamfile_header['RG']
    if len(readgroup_dict_list) < 1:
        msg = "No readgroups found."
        raise ValueError(msg)

    json_file = "{}.json"
    for readgroup_dict in readgroup_dict_list:
        missing_keys = check_readgroup(readgroup_dict.keys())
        if missing_keys:
            pass
        bam_id = readgroup_dict['ID']
        readgroup_json_file = json_file.format(bam_id.replace('+', ''))
        with _di.open(readgroup_json_file, 'w') as f:
            json.dump(readgroup_dict, f, ensure_ascii=False)
    return


def convert_readgroup_to_dict():
    """
    Possible codes:
    ID, BC, CN, DS, DT, FO, KS, LB, PG, PI, PL, PM, PU, SM
    """
    readgroup_dict_list = samfile_header['RG']
    for readgroup_dict in readgroup_dict_list:
        # logger.info('readgroup_dict=%s' % readgroup_dict)
        # check_readgroup(readgroup_dict, logger)
        readgroup_json_file = readgroup_dict['ID'] + '.json'
        readgroup_json_file = readgroup_json_file.replace('+', '')
        logger.info('readgroup_json_file=%s\n' % readgroup_json_file)
        with open(readgroup_json_file, 'w') as f:
            json.dump(readgroup_dict, f, ensure_ascii=False)
    return
