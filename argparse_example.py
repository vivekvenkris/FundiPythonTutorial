#python3 argparse_example.py 

import argparse

# help flag provides flag help
# store_true actions stores argument as True

import sys

args = sys.argv
print(args)

parser = argparse.ArgumentParser()
   
parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")
parser.add_argument('-n', '--name', type=str, required=True,  help="Your Name")


args = parser.parse_args(args[1:])

out_str = "Hello, {}!".format(args.name)
if args.output:
    print(out_str)
    
