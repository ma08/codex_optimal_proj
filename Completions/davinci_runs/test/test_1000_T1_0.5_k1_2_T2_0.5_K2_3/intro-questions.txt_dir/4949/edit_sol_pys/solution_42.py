

"""
ID: neelkolhe
TASK: 
LANG: PYTHON3
"""

inpFile=open('milk3.in','r')
outFile=open('milk3.out','w')

buckets=inpFile.readline().split()
bucketA=int(buckets[0])
bucketB=int(buckets[1])
bucketC=int(buckets[2])

for i in range(numMatches):
  length=int(inpFile.readline())
  if length<=width or length<=height or length**2<=(width**2+height**2):
    outFile.write("DA\n")
  else:
    outFile.write("NE\n")
