#!/bin/bash

# To run this script, you need to install the following tools:
#
#   * GNU parallel
#   * GNU wget
#
# This script will download all files from the website listed in the
# file 'websites.txt', and save them in the directory 'sites/'.
#
# It will also run the following commands on each file:
#
#   * sed 's/foo/bar/g'
#   * sed 's/foo/bar/g'
#
# This script will also use GNU parallel to run the commands in parallel.
#
# This script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this script.  If not, see <http://www.gnu.org/licenses/>.

set -e

echo "Downloading all files from the websites listed in 'websites.txt'..."

mkdir -p sites

# Download all files
cat websites.txt | parallel --gnu 'wget -P sites/ {}'

echo "Done."
echo

echo "Running sed commands on all files..."

# Run sed command on all files
parallel --gnu --line-buffer --progress sed -i 's/foo/bar/g' sites/*
parallel --gnu --line-buffer --progress sed -i 's/foo/bar/g' sites/*

echo "Done."
echo

echo
echo "All done."
