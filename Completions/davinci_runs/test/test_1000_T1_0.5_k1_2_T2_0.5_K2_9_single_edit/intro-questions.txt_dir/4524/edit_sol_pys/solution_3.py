#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 University of Dundee & Open Microscopy Environment.
#                    All Rights Reserved.
# Use is subject to license terms supplied in LICENSE.txt
#

"""
FOR TRAINING PURPOSES ONLY!
"""

# This is a 'bare-bones' template to allow easy conversion from a simple
# client-side Python script to a script run by the server, on the OMERO
# scripting service.
# To use the script, simply paste the body of the script (not the connection
# code) into the point indicated below.
# A more complete template, for 'real-world' scripts, is also included in this
# folder
# This script takes an Image ID as a parameter from the scripting service.
from omero.rtypes import rlong, rstring, unwrap, robject
from omero.gateway import BlitzGateway, MapAnnotationWrapper
import omero.scripts as scripts
import omero

# Script definition

# Script name, description and parameters are defined here.
# These parameters will be recognised by the Insight and web clients and
# populated with the currently selected Image(s)

# this script only takes Object (Image) IDs as input
data_types = [rstring('Dataset')]
client = scripts.client(
    'File_Download.py',
    """Download a file from the server and save to the client""",
    # first parameter
    scripts.String(
        "Data_Type", grouping="1", optional=False, values=data_types, default="Image"),
    # second parameter
    scripts.List("IDs", grouping="2", optional=False).ofType(rlong(0)),
    )

# we can now create our Blitz Gateway by wrapping the client object
conn = BlitzGateway(client_obj=client)
script_params = client.getInputs(unwrap=True)
print script_params

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# we can now create our Blitz Gateway by wrapping the client object
conn = BlitzGateway(client_obj=client)
script_params = client.getInputs(unwrap=True)
print script_params

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput("IDs"))

# get the 'IDs' parameter (which we have restricted to 'Image' IDs)
ids = unwrap(client.getInput
