# firewall.py

import argparse

parser = argparse.ArgumentParser(description='rules for firewall')
parser.add_argument('-l --logfile', type=str, help='Input dir for files')
parser.add_argument('-r --rules', type=str, help='Output dir for rules')
args = parser.parse_args()
print(args.l logfile)