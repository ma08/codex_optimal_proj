import os
import sys
import re


def openfile():
    try:
        f = open("/home/michael/c++_test/test.txt", "r")
        return f
    except:
        print("Error: file does not exist")
        return


def readfile(f):
    try:
        lines = f.readlines()
        return lines
    except:
        print("Error: could not read file")
        return


def check_for_errors(f):
    try:
        lines = readfile(f)
        if lines == None:
            print("Error: could not read file")
            return
        else:
            for line in lines:
                if re.search("^\s*$", line):
                    print("Warning: empty line")
                if re.search("^\s*#", line):
                    print("Warning: line starts with #")
                if re.search("using namespace", line):
                    print("Warning: using namespace")
                if re.search("^\s*for", line):
                    print("Warning: for loop")
                if re.search("^\s*while", line):
                    print("Warning: while loop")
                if re.search("^\s*if", line):
                    print("Warning: if condition")
                if re.search("^\s*else", line):
                    print("Warning: else condition")
                if re.search("^\s*return", line):
                    print("Warning: return statement")
                if re.search("^\s*break", line):
                    print("Warning: break statement")
                if re.search("^\s*continue", line):
                    print("Warning: continue statement")
                if re.search("^\s*switch", line):
                    print("Warning: switch statement")
                if re.search("^\s*case", line):
                    print("Warning: case statement")
                if re.search("^\s*default", line):
                    print("Warning: default statement")
                if re.search("^\s*try", line):
                    print("Warning: try statement")
                if re.search("^\s*catch", line):
                    print("Warning: catch statement")
                if re.search("^\s*throw", line):
                    print("Warning: throw statement")
                if re.search("^\s*do", line):
                    print("Warning: do statement")
                if re.search("^\s*new", line):
                    print("Warning: new statement")
                if re.search("^\s*delete", line):
                    print("Warning: delete statement")
                if re.search("^\s*goto", line):
                    print("Warning: goto statement")
                if re.search("^\s*const", line):
                    print("Warning: constant statement")
                if re.search("^\s*static", line):
                    print("Warning: static statement")
                if re.search("^\s*auto", line):
                    print("Warning: auto statement")
                if re.search("^\s*extern", line):
                    print("Warning: extern statement")
                if re.search("^\s*register", line):
                    print("Warning: register statement")
                if re.search("^\s*volatile", line):
                    print("Warning: volatile statement")
                if re.search("^\s*typedef", line):
                    print("Warning: typedef statement")
                if re.search("^\s*sizeof", line):
                    print("Warning: sizeof statement")
                if re.search("^\s*this", line):
                    print("Warning: this statement")
    except:
        print("Error: could not check file for errors")
        return


def main():
    try:
        f = openfile()
        if f == None:
            print("Error: could not read file")
            return
        else:
            check_for_errors(f)
    except:
        print("Error: could not check file for errors")
        return


main()
