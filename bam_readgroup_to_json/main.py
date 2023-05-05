#!/usr/bin/env python

import argparse
import json
import logging
import os
import sys

import pysam


def check_readgroup(readgroup_dict: dict, logger: logging.Logger) -> None:
    required_fields = ("CN", "ID", "LB", "PL", "PU", "SM")
    for field in required_fields:
        if field not in readgroup_dict:
            logger.info(f"{field} is missing from readgroup")
            sys.exit(1)
    return


def legacy_check_readgroup(readgroup_dict: dict, logger: logging.Logger) -> None:
    required_fields = ("CN", "ID", "LB", "PL", "SM")
    for field in required_fields:
        if field not in readgroup_dict:
            logger.info(f"{field} is missing from readgroup")
            sys.exit(1)
    return


def extract_readgroup_json(bam_path: str, logger: logging.Logger) -> None:
    bam_file = os.path.basename(bam_path)
    bam_name, _ = os.path.splitext(bam_file)
    samfile = pysam.AlignmentFile(bam_path, "rb", check_sq=False)
    samfile_header = samfile.header
    readgroup_dict_list = samfile_header["RG"]
    if len(readgroup_dict_list) < 1:
        logger.debug(f"There are no readgroups in BAM: {bam_name}")
        logger.debug(f"\treadgroup: {readgroup_dict_list}")
        sys.exit(1)
    else:
        for readgroup_dict in readgroup_dict_list:
            logger.info(f"{readgroup_dict=}")
            check_readgroup(readgroup_dict, logger)
            readgroup_json_file = f"{readgroup_dict['ID']}.json".replace("+", "")
            logger.info(f"{readgroup_json_file=}")
            with open(readgroup_json_file, "w") as f:
                json.dump(readgroup_dict, f, ensure_ascii=False)
    return


def header_rg_list_to_rg_dicts(header_rg_list: list) -> list:
    readgroups_list = list()
    for rg_list in header_rg_list:
        keys_values = (
            rg_list.lstrip("@RG").lstrip("\t").lstrip("@SQ").lstrip("\t").split("\t")
        )
        readgroup = dict()
        for key_value in keys_values:
            key_value_split = key_value.split(":")
            a_key = key_value_split[0]
            a_value = key_value_split[1]
            readgroup[a_key] = a_value
        if "PL" not in readgroup:
            readgroup["PL"] = "ILLUMINA"
        readgroups_list.append(readgroup)
    return readgroups_list


def legacy_extract_readgroup_json(bam_path: str, logger: logging.Logger) -> None:
    bam_file = os.path.basename(bam_path)
    bam_name, _ = os.path.splitext(bam_file)
    samfile = pysam.AlignmentFile(bam_path, "rb", check_sq=False)
    samfile_header = samfile.text
    header_list = samfile_header.split("\n")
    header_rg_list = [
        header_line for header_line in header_list if header_line.startswith("@RG")
    ]
    readgroup_dict_list = header_rg_list_to_rg_dicts(header_rg_list)
    if len(readgroup_dict_list) == 0:
        logger.info(f"{len(readgroup_dict_list)=}")
        readgroup_dict = dict()
        readgroup_dict["ID"] = "default"
        readgroup_json_file = "default.json"
        with open(readgroup_json_file, "w") as f:
            json.dump(readgroup_dict, f, ensure_ascii=False)
    else:
        for readgroup_dict in readgroup_dict_list:
            logger.info(f"{readgroup_dict=}" % readgroup_dict)
            # legacy_check_readgroup(readgroup_dict, logger)
            readgroup_json_file = readgroup_dict["ID"] + ".json"
            readgroup_json_file = readgroup_json_file.replace("+", "")
            logger.info("readgroup_json_file=%s\n" % readgroup_json_file)
            with open(readgroup_json_file, "w") as f:
                json.dump(readgroup_dict, f, ensure_ascii=False)
    return


def setup_logging(args: argparse.Namespace) -> logging.Logger:
    logging.basicConfig(
        filename=os.path.join("output.log"),
        level=args.level,
        filemode="w",
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d_%H:%M:%S_%Z",
    )
    logger = logging.getLogger(__name__)
    return logger


def main() -> int:
    parser = argparse.ArgumentParser("convert readgroups to json")

    # Logging flags.
    parser.add_argument(
        "-d",
        "--debug",
        action="store_const",
        const=logging.DEBUG,
        dest="level",
        help="Enable debug logging.",
    )
    parser.set_defaults(level=logging.INFO)

    # Required flags.
    parser.add_argument("-b", "--bam_path", required=True, help="BAM file.")
    parser.add_argument(
        "-m",
        "--mode",
        required=True,
    )

    args = parser.parse_args()
    bam_path = args.bam_path
    mode = args.mode

    logger = setup_logging(args)

    if mode == "strict":
        extract_readgroup_json(bam_path, logger)
    elif mode == "lenient":
        legacy_extract_readgroup_json(bam_path, logger)
    return 0


if __name__ == "__main__":
    main()
