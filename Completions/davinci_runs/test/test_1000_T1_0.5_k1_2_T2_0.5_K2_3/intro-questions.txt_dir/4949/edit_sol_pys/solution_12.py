

"""
ID: neelkolhe
TASK: 
LANG: PYTHON3
"""

inpFile=open('matches.in', 'r')
outFile=open('matches.out', 'w')

numMatches=int(inpFile.readline().rstrip())
dimensions=inpFile.readline().split()
width=int(dimensions[0].rstrip())
height=int(dimensions[1].rstrip())

for i in range(numMatches):
  length=int(inpFile.readline().rstrip())
  if length<=width or length<=height or (length**2<=(width**2+height**2)):
    outFile.write("DA\n")
  else:
    outFile.write("NE\n")
