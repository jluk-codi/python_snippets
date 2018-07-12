from __future__ import print_function

###############
# CLI args
###############

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("target_manifest_path", nargs="?")
args = parser.parse_args()

###############
# Logging
###############

import logging

def set_logging(args):
    log_filename = '/var/log/artifact_curator.log'

    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG

    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)

    logger.addHandler(console)
    if log_level is not logging.DEBUG:
        logger.addHandler(fh)
