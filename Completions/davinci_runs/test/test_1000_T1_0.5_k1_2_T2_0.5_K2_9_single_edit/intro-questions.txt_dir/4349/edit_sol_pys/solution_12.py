#!/bin/bash

# Script error handling
set -o errexit
set -o pipefail
set -o nounset

# Script variables
readonly SCRIPT_NAME=$(basename $0)
readonly SCRIPT_DIR=$(cd $(dirname $0) && pwd)
readonly SCRIPT_ARGS="$@"

# Check if the script is running as root
if [ $(id -u) -ne 0 ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run as root"
    exit 1
fi

# Check if the script is running in a TTY
if [ ! -t 1 ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a TTY"
    exit 1
fi

# Check if the script is running in a valid terminal
if [ "$TERM" != "xterm" ] && [ "$TERM" != "xterm-256color" ] && [ "$TERM" != "screen" ] && [ "$TERM" != "screen-256color" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a valid terminal"
    exit 1
fi

# Check if the script is running in a valid shell
if [ "$SHELL" != "/bin/bash" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in bash"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$SCRIPT_DIR" != "/root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in /root"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$(ls -A)" != "" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in an empty directory"
    exit 1
fi

# Check if the script is running with no arguments
if [ "$SCRIPT_ARGS" != "" ]; then
    echo "ERROR: $SCRIPT_NAME does not accept arguments"
    exit 1
fi

# Check if the script is running as root
if [ "$(whoami)" != "root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run as root"
    exit 1
fi

# Check if the script is running in a TTY
if [ ! -t 0 ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a TTY"
    exit 1
fi

# Check if the script is running in a valid terminal
if [ "$TERM" != "xterm" ] && [ "$TERM" != "xterm-256color" ] && [ "$TERM" != "screen" ] && [ "$TERM" != "screen-256color" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a valid terminal"
    exit 1
fi

# Check if the script is running in a valid shell
if [ "$SHELL" != "/bin/bash" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in bash"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$SCRIPT_DIR" != "/root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in /root"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$(ls -A)" != "" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in an empty directory"
    exit 1
fi

# Check if the script is running with no arguments
if [ "$SCRIPT_ARGS" != "" ]; then
    echo "ERROR: $SCRIPT_NAME does not accept arguments"
    exit 1
fi

# Check if the script is running as root
if [ "$(whoami)" != "root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run as root"
    exit 1
fi

# Check if the script is running in a TTY
if [ ! -t 0 ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a TTY"
    exit 1
fi

# Check if the script is running in a valid terminal
if [ "$TERM" != "xterm" ] && [ "$TERM" != "xterm-256color" ] && [ "$TERM" != "screen" ] && [ "$TERM" != "screen-256color" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a valid terminal"
    exit 1
fi

# Check if the script is running in a valid shell
if [ "$SHELL" != "/bin/bash" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in bash"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$SCRIPT_DIR" != "/root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in /root"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$(ls -A)" != "" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in an empty directory"
    exit 1
fi

# Check if the script is running with no arguments
if [ "$SCRIPT_ARGS" != "" ]; then
    echo "ERROR: $SCRIPT_NAME does not accept arguments"
    exit 1
fi

# Check if the script is running as root
if [ "$(whoami)" != "root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run as root"
    exit 1
fi

# Check if the script is running in a TTY
if [ ! -t 0 ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a TTY"
    exit 1
fi

# Check if the script is running in a valid terminal
if [ "$TERM" != "xterm" ] && [ "$TERM" != "xterm-256color" ] && [ "$TERM" != "screen" ] && [ "$TERM" != "screen-256color" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a valid terminal"
    exit 1
fi

# Check if the script is running in a valid shell
if [ "$SHELL" != "/bin/bash" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in bash"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$SCRIPT_DIR" != "/root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in /root"
    exit 1
fi

# Check if the script is running in a valid directory
if [ "$(ls -A)" != "" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in an empty directory"
    exit 1
fi

# Check if the script is running with no arguments
if [ "$SCRIPT_ARGS" != "" ]; then
    echo "ERROR: $SCRIPT_NAME does not accept arguments"
    exit 1
fi

# Check if the script is running as root
if [ "$(whoami)" != "root" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run as root"
    exit 1
fi

# Check if the script is running in a TTY
if [ ! -t 0 ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a TTY"
    exit 1
fi

# Check if the script is running in a valid terminal
if [ "$TERM" != "xterm" ] && [ "$TERM" != "xterm-256color" ] && [ "$TERM" != "screen" ] && [ "$TERM" != "screen-256color" ]; then
    echo "ERROR: $SCRIPT_NAME needs to be run in a valid terminal"
