#!/usr/bin/env python3

import argparse
import sys
import os

def compile_python(input_file):
    with open(input_file, 'r', encoding="UTF-8") as input_fd:
        for line in input_fd.readlines():
            [key, value] = line.strip().split('=')
            print(f"{key} = '{value}'")

def compile_to(input_file, fmt):
    if fmt == 'python':
        compile_python(input_file)
    else:
        sys.stderr.write(f"unknown format: {fmt}\n")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Output branding environment ' \
                                                 'variables in various formats')
    parser.add_argument('input',
                        help='Branding input file',
                        nargs='?',
                        default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                             'branding'))
    parser.add_argument('--format',
                        default='python',
                        help='Output format')

    args = parser.parse_args()
    compile_to(args.input, args.format)

if __name__ == "__main__":
    main()
