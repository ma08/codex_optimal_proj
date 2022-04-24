#!/bin/bash

# This is a simple bash script to fix the syntax errors in the files.
# It is used to fix the syntax error in the files.

# Author : Praveen Kumar Pendyala
# Email  : praveen.pendyala@gmail.com

# Usage : ./fix_syntax.sh <file_name>

# Exit if any command fails.
set -e

# Exit if any variable is not set.
set -u

# Exit if any command in a pipe fails.
set -o pipefail

# Set the input file name.
FILE_NAME="$1"

# Set the output file name.
OUTPUT_FILE_NAME="$FILE_NAME.fixed"

# Set the sed command to remove the extra spaces.
SED_COMMAND="s/\s\+/ /g"

# Remove the extra spaces in the file.
sed -r "$SED_COMMAND" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
sed -r "s/\s$//g" "$FILE_NAME" > "$OUTPUT_FILE_NAME"

# Remove the extra spaces in the beginning of the lines.
sed -r "s/^\s//g" "$OUTPUT_FILE_NAME" > "$FILE_NAME"

# Remove the extra spaces in the end of the lines.
