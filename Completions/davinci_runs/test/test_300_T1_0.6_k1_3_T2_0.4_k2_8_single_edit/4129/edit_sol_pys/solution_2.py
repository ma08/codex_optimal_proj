#!/usr/bin/env python

import os
import sys
import requests
import shutil


def download_file(url, directory):
    """
    This function downloads a file from a given URL and saves it to a given
    directory.
    """
    local_filename = url.split('/')[-1]
    local_path = os.path.join(directory, local_filename)
    r = requests.get(url, stream=True)
    with open(local_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    return local_path


def main():
    # Read the command line arguments
    url = sys.argv[1]
    directory = sys.argv[2]

    # Download the file
    file_path = download_file(url, directory)

    # Print the file path
    print(file_path)


if __name__ == '__main__':
    main()
