

"""
ID: neelkolhe
TASK: matches
LANG: PYTHON3
"""

inpFile=open('matches.in', 'r')
outFile=open('matches.out', 'w')

numMatches=int(inpFile.readline())
dimensions=inpFile.readline().split()
width=int(dimensions[0])
height=int(dimensions[1])

for i in range(numMatches):
  length=int(inpFile.readline())  
  if length<=width or length<=height or length<=(width**2+height**2)**0.5: outFile.write("DA\n") 
  else: outFile.write("NE\n") 
