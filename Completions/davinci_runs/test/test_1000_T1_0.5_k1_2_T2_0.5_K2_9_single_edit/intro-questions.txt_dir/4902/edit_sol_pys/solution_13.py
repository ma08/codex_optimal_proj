import os
import sys
import filecmp
import subprocess
import time


# This is a simple tester for the Unix 'sort' command.
# It runs 'sort' on a few test cases and checks its output and exit status.

# Location of the program to test
prog = './sort'

# Temporary file folder
tmp = '/tmp/sort/'

# Simple test case
testcase1in  = '1 2 3 4\n'
testcase1out = '1 2 3 4\n'

# Simple test case
testcase2in  = '4 3 2 1\n'
testcase2out = '1 2 3 4\n'

# Simple test case
testcase3in  = '1 3 2 4\n'
testcase3out = '1 2 3 4\n'

# Simple test case
testcase4in  = '4 2 3 1\n'
testcase4out = '1 2 3 4\n'

# Simple test case
testcase5in  = '1 2 3 4\n'
testcase5out = '1 2 3 4\n'

# Simple test case
testcase6in  = '4 3 2 1\n'
testcase6out = '1 2 3 4\n'

# Simple test case
testcase7in  = '1 3 2 4\n'
testcase7out = '1 2 3 4\n'

# Simple test case
testcase8in  = '4 2 3 1\n'
testcase8out = '1 2 3 4\n'

# Simple test case
testcase9in  = '1 2 3 4\n'
testcase9out = '1 2 3 4\n'

# Simple test case
testcase10in  = '4 3 2 1\n'
testcase10out = '1 2 3 4\n'

# Simple test case
testcase11in  = '1 3 2 4\n'
testcase11out = '1 2 3 4\n'

# Simple test case
testcase12in  = '4 2 3 1\n'
testcase12out = '1 2 3 4\n'

# Simple test case
testcase13in  = '1 2 3 4\n'
testcase13out = '1 2 3 4\n'

# Simple test case
testcase14in  = '4 3 2 1\n'
testcase14out = '1 2 3 4\n'

# Simple test case
testcase15in  = '1 3 2 4\n'
testcase15out = '1 2 3 4\n'

# Simple test case
testcase16in  = '4 2 3 1\n'
testcase16out = '1 2 3 4\n'

# Simple test case
testcase17in  = '1 2 3 4\n'
testcase17out = '1 2 3 4\n'

# Simple test case
testcase18in  = '4 3 2 1\n'
testcase18out = '1 2 3 4\n'

# Simple test case
testcase19in  = '1 3 2 4\n'
testcase19out = '1 2 3 4\n'

# Simple test case
testcase20in  = '4 2 3 1\n'
testcase20out = '1 2 3 4\n'

# Simple test case
testcase21in  = '1 2 3 4\n'
testcase21out = '1 2 3 4\n'

# Simple test case
testcase22in  = '4 3 2 1\n'
testcase22out = '1 2 3 4\n'

# Simple test case
testcase23in  = '1 3 2 4\n'
testcase23out = '1 2 3 4\n'

# Simple test case
testcase24in  = '4 2 3 1\n'
testcase24out = '1 2 3 4\n'

# Simple test case
testcase25in  = '1 2 3 4\n'
testcase25out = '1 2 3 4\n'

# Simple test case
testcase26in  = '4 3 2 1\n'
testcase26out = '1 2 3 4\n'

# Simple test case
testcase27in  = '1 3 2 4\n'
testcase27out = '1 2 3 4\n'

# Simple test case
testcase28in  = '4 2 3 1\n'
testcase28out = '1 2 3 4\n'

# Simple test case
testcase29in  = '1 2 3 4\n'
testcase29out = '1 2 3 4\n'

# Simple test case
testcase30in  = '4 3 2 1\n'
testcase30out = '1 2 3 4\n'

# Simple test case
testcase31in  = '1 3 2 4\n'
testcase31out = '1 2 3 4\n'

# Simple test case
testcase32in  = '4 2 3 1\n'
testcase32out = '1 2 3 4\n'

# Simple test case
testcase33in  = '1 2 3 4\n'
testcase33out = '1 2 3 4\n'

# Simple test case
testcase34in  = '4 3 2 1\n'
testcase34out = '1 2 3 4\n'

# Simple test case
testcase35in  = '1 3 2 4\n'
testcase35out = '1 2 3 4\n'

# Simple test case
testcase36in  = '4 2 3 1\n'
testcase36out = '1 2 3 4\n'

# Simple test case
testcase37in  = '1 2 3 4\n'
testcase37out = '1 2 3 4\n'

# Simple test case
testcase38in  = '4 3 2 1\n'
testcase38out = '1 2 3 4\n'

# Simple test case
testcase39in  = '1 3 2 4\n'
testcase39out = '1 2 3 4\n'

# Simple test case
testcase40in  = '4 2 3 1\n'
testcase40out = '1 2 3 4\n'


# Run a test case
def runtest(inp, outp):
    """Run test case and check output"""
    # Write input to temp file
    tmpin = tmp + 'in'
    with open(tmpin, 'w') as f:
        f.write(inp)

    # Run program on input file
    tmppout = tmp + 'out'
    retval = subprocess.call([prog], stdin=open(tmpin), stdout=open(tmppout, 'w'))

    # Compare program output with output file
    success = filecmp.cmp(tmppout, outp)

    # Clean up temp files
    os.remove(tmpin)
    os.remove(tmppout)

    return success, retval
