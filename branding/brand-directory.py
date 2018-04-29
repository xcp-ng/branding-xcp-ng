#!/usr/bin/env python

import argparse
import os
import shutil
import sys

def replace_values(line, dictionary):
    """
    For each (key, value) in dictionary, replace @key@ with value in line.
    """
    output = line

    for key, value in dictionary.items():
        search = "@" + key + "@"
        output = output.replace(search, value)

    return output

def brand_directory(inputfile, fromdir, todir):
    branding = {}
    with open(inputfile, 'r') as inputfd:
        for line in inputfd.readlines():
            [key, value] = line.strip().split('=')
            branding[key] = value

    if fromdir[len(fromdir) - 1] != "/":
        fromdir = fromdir + "/"

    if not os.path.isdir(todir):
        os.mkdir(todir)
    for root, directories, files in os.walk(fromdir):
        todir_root = os.path.join(todir, root[len(fromdir):])

        # make directories at the destination
        for directory in directories:
            new_directory = os.path.join(todir_root, directory)
            if not os.path.isdir(new_directory):
                os.mkdir(new_directory)

        # copy files to the destination
        for file in files:
            fromfile = os.path.join(root, file)
            tofile = os.path.join(todir_root, file)

            with open(fromfile, 'r') as fromfd:
                with open(tofile, 'w') as tofd:
                    for fromline in fromfd.readlines():
                        toline = replace_values(fromline, branding)
                        tofd.write(toline)

            # copy the file permissions
            shutil.copymode(fromfile, tofile)

def fail_with_message(message):
    print message
    sys.exit(1)

def usage():
    print "usage:"
    print "  %s <inputfile> <fromdir> <todir>" % sys.argv[0]
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()

    inputfile = sys.argv[1]
    fromdir   = sys.argv[2]
    todir     = sys.argv[3]

    if not os.path.isdir(fromdir):
        fail_with_message("%s is not a directory" % fromdir)
    else:
        brand_directory(inputfile, fromdir, todir)
