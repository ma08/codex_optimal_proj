#!/usr/bin/python

import os
import time
import sys

print "Content-type: text/html\n\n"
print "<html>"
print "<head>"
print "<title>File Manager</title>"
print "</head>"
print "<body>"
print "<h1>File Manager</h1>"
print "<form enctype='multipart/form-data' action='file.py' method='POST'>"
print "<p>File: <input type='file' name='file'></p>"
print "<p><input type='submit' value='Upload'></p>"
print "</form>"
print "<hr>"
print "<h2>File List</h2>"
print "<table>"
print "<tr><th>File</th><th>Size</th><th>Last Modified</th></tr>"

for file in os.listdir("."):
    if file.endswith(".txt"):
        stats = os.stat(file)
        print "<tr><td><a href='file.py?file=" + file + "'>" + file + "</a></td><td>" + str(stats.st_size) + "</td><td>" + time.ctime(stats.st_mtime) + "</td></tr>"

print "</table>"

print "<hr>"
print "<h2>File Viewer</h2>"

if "file" in os.environ["QUERY_STRING"]:
    print "<p>File: " + os.environ["QUERY_STRING"].split("=")[1] + "</p>"
    print "<pre>"
    file = open(os.environ["QUERY_STRING"].split("=")[1], "r")
    print file.read()
    file.close()
    print "</pre>"

print "<hr>"

print "<h2>File Uploader</h2>"

if "file" in os.environ["REQUEST_METHOD"]:
    print "<p>Successfully uploaded " + os.environ["CONTENT_LENGTH"] + " bytes.</p>"

print "</body>"
print "</html>"
