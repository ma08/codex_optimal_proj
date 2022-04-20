#!/usr/bin/python

import re
import os
import sys
import subprocess

# This script is to extract the number of the last commit
# from the file "commit.txt" and then to compare with the
# number of the commit of the current commit.
# If the current commit is newer, the script will do the
# following things:
#   1. update the file "commit.txt" with the number of
#      the current commit
#   2. update the file "commit_date.txt" with the date
#      of the current commit
#   3. update the file "commit_author.txt" with the author
#      of the current commit
#   4. update the file "commit_message.txt" with the message
#      of the current commit
#   5. update the file "commit_files.txt" with the files
#      of the current commit
#   6. update the file "commit_link.txt" with the link of
#      the current commit
# If the current commit is not newer, the script will do
# nothing.

# get the number of the last commit
f = open('commit.txt', 'r')
last_commit = f.readline()
f.close()

# get the number of the current commit
current_commit = subprocess.check_output(["git", "rev-parse", "HEAD"])

# get the date of the current commit
current_date = subprocess.check_output(["git", "log", "-1", "--format=%cd"])

# get the author of the current commit
current_author = subprocess.check_output(["git", "log", "-1", "--format=%an"])

# get the message of the current commit
current_message = subprocess.check_output(["git", "log", "-1", "--format=%B"])

# get the files of the current commit
current_files = subprocess.check_output(["git", "log", "-1", "--name-only", "--format=%B"])

# get the link of the current commit
current_link = subprocess.check_output(["git", "log", "-1", "--format=%H"])

# remove the '\n' at the end of the strings
last_commit = last_commit.rstrip()
current_commit = current_commit.rstrip()
current_date = current_date.rstrip()
current_author = current_author.rstrip()
current_message = current_message.rstrip()
current_files = current_files.rstrip()
current_link = current_link.rstrip()

# compare the current commit with the last commit
if current_commit != last_commit:
    # update the file "commit.txt" with the number of the current commit
    f = open('commit.txt', 'w')
    f.write(current_commit)
    f.close()
    # update the file "commit_date.txt" with the date of the current commit
    f = open('commit_date.txt', 'w')
    f.write(current_date)
    f.close()
    # update the file "commit_author.txt" with the author of the current commit
    f = open('commit_author.txt', 'w')
    f.write(current_author)
    f.close()
    # update the file "commit_message.txt" with the message of the current commit
    f = open('commit_message.txt', 'w')
    f.write(current_message)
    f.close()
    # update the file "commit_files.txt" with the files of the current commit
    f = open('commit_files.txt', 'w')
    f.write(current_files)
    f.close()
    # update the file "commit_link.txt" with the link of the current commit
    f = open('commit_link.txt', 'w')
    f.write(current_link)
    f.close()


