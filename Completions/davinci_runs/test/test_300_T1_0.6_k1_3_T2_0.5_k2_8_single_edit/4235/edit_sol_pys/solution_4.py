#!/bin/bash

# 
#   Copyright 2016 RIFT.IO Inc
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

#
# @file file.sh
# @author Varun Prasad (varun.prasad@riftio.com)
# @date 11/19/2015
# @brief File Utilities
#

# @brief Check if file exists
#
# @param $1 file path
#
# @returns 0 if file exists; 1 otherwise
#
function file_exists() {
    local file="$1"
    [[ -f "$file" ]] && return 0
    return 1
}

# @brief Check if directory exists
#
# @param $1 directory path
#
# @returns 0 if directory exists; 1 otherwise
#
function directory_exists() {
    local directory="$1"
    [[ -d "$directory" ]] && return 0
    return 1
}

# @brief Check if file or directory exists
#
# @param $1 file or directory path
#
# @returns 0 if file or directory exists; 1 otherwise
#
function path_exists() {
    local path="$1"
    [[ -e "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is readable
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is readable; 1 otherwise
#
function path_readable() {
    local path="$1"
    [[ -r "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is writable
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is writable; 1 otherwise
#
function path_writable() {
    local path="$1"
    [[ -w "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is executable
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is executable; 1 otherwise
#
function path_executable() {
    local path="$1"
    [[ -x "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is empty
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is empty; 1 otherwise
#
function path_empty() {
    local path="$1"
    [[ -z "$(ls -A $path)" ]] && return 0
    return 1
}

# @brief Check if file or directory is a symbolic link
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a symbolic link; 1 otherwise
#
function path_symlink() {
    local path="$1"
    [[ -L "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is a socket
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a socket; 1 otherwise
#
function path_socket() {
    local path="$1"
    [[ -S "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is a pipe
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a pipe; 1 otherwise
#
function path_pipe() {
    local path="$1"
    [[ -p "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is a block device
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a block device; 1 otherwise
#
function path_block_device() {
    local path="$1"
    [[ -b "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is a character device
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a character device; 1 otherwise
#
function path_character_device() {
    local path="$1"
    [[ -c "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is a named pipe
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a named pipe; 1 otherwise
#
function path_named_pipe() {
    local path="$1"
    [[ -p "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is a socket
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a socket; 1 otherwise
#
function path_socket() {
    local path="$1"
    [[ -S "$path" ]] && return 0
    return 1
}

# @brief Check if file or directory is a symbolic link
#
# @param $1 file or directory path
#
# @returns 0 if file or directory is a symbolic link; 1 otherwise
#
function path_symlink() {
    local path="$1"
    [[ -L "$path" ]] && return 0
    return 1
}
