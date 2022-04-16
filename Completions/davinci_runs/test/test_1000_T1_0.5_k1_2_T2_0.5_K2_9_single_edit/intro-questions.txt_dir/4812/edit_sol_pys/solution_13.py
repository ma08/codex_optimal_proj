"""
ID: neelkolhe
TASK: test
"""


inpFile=open('test.in','r')
outFile=open('test.out','w')


a, b = (int(x) for x in inpFile.read().split())
outFile.write(str(a+b) + '\n')
