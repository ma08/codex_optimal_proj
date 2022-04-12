

"""
ID: neelkolhe
TASK: ride
"""


inpFile=open('ride.in','r')
outFile=open('ride.out','w')



comet=inpFile.readline().strip()
group=inpFile.readline().strip()

def checkRide(comet,group):
  cometNum=1
  groupNum=1
  for i in range(len(comet)):
    cometNum=cometNum*(ord(comet[i])-64)
  for i in range(len(group)):
    groupNum=groupNum*(ord(group[i])-64)
  if cometNum%47==groupNum%47:
    outFile.write("GO\n") 
  else:
    outFile.write("STAY\n")

checkRide(comet,group)
