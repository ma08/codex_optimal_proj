#!/bin/bash

# Install a custom File version - https://www.darwinsys.com/file/
#
# To run this script on Codeship, add the following
# command to your project's setup commands:
# \curl -sSL https://raw.githubusercontent.com/codeship/scripts/master/packages/file.sh | bash -s
#
# Add the following environment variable to your project configuration
# (otherwise the default below will be used).
# * FILE_VERSION
#
FILE_VERSION=${FILE_VERSION:="5.30"}
FILE_DIR=${FILE_DIR:=$HOME/cache/file}

set -e

CACHED_DOWNLOAD="${HOME}/cache/file-${FILE_VERSION}.tar.gz"

mkdir -p "${FILE_DIR}"
wget --continue --output-document "${CACHED_DOWNLOAD}" "https://darwinsys.com/file/file-${FILE_VERSION}.tar.gz"
tar -xaf "${CACHED_DOWNLOAD}" --strip-components=1 --directory "${FILE_DIR}"

(
  cd "${FILE_DIR}" || exit 1
  ./configure --prefix="${HOME}/file"
  make install
)
