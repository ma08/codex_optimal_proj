#!/usr/bin/env python

import sys
import os
import json

def main(argv):
    if len(argv) < 2:
        print "Usage: %s <file>" % argv[0]
        sys.exit(1)
    path = argv[1]

    if not os.path.exists(path):
        print "File %s doesn't exist" % path
        sys.exit(1)

    print json.dumps({"changed": False, "failed": False, "msg": "File %s exists" % path})
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
