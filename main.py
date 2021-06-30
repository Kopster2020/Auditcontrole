#!/usr/bin/python3
import argparse
import sys
from device import Device

'Command start the proces. Change arg1 for diffrent config and arg2 for another baseline file specfice for other deveicetypes and venders '
'python main.py RouterTestConf.txt baseline.json'

def parseInputArgs(argv):
    parser = argparse.ArgumentParser(description="Test Automatic Audit")
    parser.add_argument('config')
    parser.add_argument('baseline')
    args = parser.parse_args()
    return args

def exec(inputArgs):
    #config_file use only when testing single object
    config_file = ""
    parsed_args = parseInputArgs(inputArgs)

    if parsed_args.config:
        deviceParser = Device(parsed_args.config, parsed_args.baseline)
        deviceParser.performAudit()
        deviceParser.output()

def main():
    exec(sys.argv[1:])

if __name__ == "__main__":
    main()

