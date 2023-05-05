#!/usr/bin/env python
"""
Python Project Template Entrypoint Script
"""

import datetime
import logging
import sys

import click

from bam_readgroup_to_json.main import (
    extract_readgroup_json,
    legacy_extract_readgroup_json,
)

try:
    from bam_readgroup_to_json import __version__
except Exception:
    __version__ = "0.0.0"

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s:%(lineno)s %(levelname)s | %(message)s",
)


def run(
    bam_path: str,
    mode: str,
) -> int:
    """Method for running script logic.

    Accepts:
        run_args (namespace): Collection of parsed arguments
    Returns:
        ret_code (int): Return code for sys.exit()
    """

    ret_val = 0

    start_time = datetime.datetime.now()

    logger.info("Running process...")

    if mode == "strict":
        extract_readgroup_json(bam_path, logger)
    elif mode == "lenient":
        legacy_extract_readgroup_json(bam_path, logger)

    end_time = datetime.datetime.now()
    run_time = end_time - start_time
    logger.info("Run time: %d seconds", run_time.seconds)
    return ret_val


@click.command()
@click.version_option(version=__version__)
@click.option("--bam-path", "--bam_path", "-b", required=True, help="Bam file")
@click.option("--mode", "-m", required=True, choices=("strict", "lenient"))
def main(
    bam_path: str,
    mode: str,
) -> int:
    """Main Entrypoint."""
    exit_code = 0
    args = sys.argv

    logger.info("Version: %s", __version__)
    logger.info("Process called with %s", args)

    try:
        exit_code = run(bam_path, mode)
    except Exception as e:
        logger.exception(e)
        exit_code = 1
    return exit_code


if __name__ == "__main__":
    """CLI Entrypoint"""

    status_code = 0
    try:
        status_code = main()
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
    sys.exit(status_code)


# __END__
