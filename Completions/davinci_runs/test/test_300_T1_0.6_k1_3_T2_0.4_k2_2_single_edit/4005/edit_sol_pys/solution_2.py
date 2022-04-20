#!/usr/bin/python

import os
import sys

# Open a file
path = "/var/log/messages"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# Close opened file
os.close( fd )



