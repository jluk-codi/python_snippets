#######
# Print function support in Python 2.x
#######

from __future__ import print_function

##########
# Read config from YAML file
##########

import yaml
config = {}
config_path = 'config.yaml'
try:
    with open(config_path, 'r') as config_file:
        config = yaml.load(config_file)
except IOError:
    print('Error reading config from', config_path)
print(config)


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

log = logging.getLogger('myname')

def set_logging(args):
    log_filename = '/var/log/artifact_curator.log'

    log.setLevel(logging.DEBUG)

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

    log.addHandler(console)
    if log_level is not logging.DEBUG:
        log.addHandler(fh)

###########################
# JSON safe pretty dump
###########################

import json

class SafeObjectEncoder(json.JSONEncoder):
    default = lambda self, obj: str(obj)

def pretty_json(obj):
    json.dumps(obj, cls=SafeObjectEncoder, indent=4)
