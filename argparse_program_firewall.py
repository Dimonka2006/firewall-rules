# firewall.py

import argparse

parser = argparse.ArgumentParser(description='rules for firewall')
parser.add_argument('-l', '--logfile', dest='logfile_list', metavar='LOGFILE', nargs=' * ', type=str, help='Input dir for files')
parser.add_argument('-r', '--rules', type=str, help='Output dir for rules')
args = parser.parse_args()
print(f'Input dir for files: {args.logfile}')
print(f'Output dir for rules: {args.rules}')
print(args.logfile_list)
