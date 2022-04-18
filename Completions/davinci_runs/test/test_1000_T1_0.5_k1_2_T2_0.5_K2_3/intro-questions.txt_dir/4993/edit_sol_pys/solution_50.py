
#!/usr/bin/python
import sys, os, time
filename = sys.argv[1]
while True:
    if os.path.exists(filename):
        print "File exists: %s" % filename
        break
    else:
        print "File not found"
        time.sleep(5)
