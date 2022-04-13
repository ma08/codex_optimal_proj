

"""
ID: neelkolhe
TASK: file
"""


inpFile=open('file.in','r')
outFile=open('file.out','w')


listOfEndings=[]
word=inpFile.readline().strip()
numOfLists=int(inpFile.readline())

listOfLists=[]

for i in range(numOfLists):
  listOfLists.append(inpFile.readline().strip().split(' '))

numOfPhrases=int(inpFile.readline())

listOfPhrases=[]

for i in range(numOfPhrases):
  listOfPhrases.append(inpFile.readline().strip().split(' '))

def checkFile(word,listOfLists,listOfPhrases):
  
  for i in range(len(listOfLists)):
    for j in range(len(listOfLists[i])):
      if listOfLists[i][j] in word and listOfLists[i][j] not in listOfEndings:
        listOfEndings.append(listOfLists[i][j])
        break
  for i in range(len(listOfPhrases)):
    for j in range(len(listOfPhrases[i])):
      for k in range(len(listOfEndings)):
        if listOfEndings[k] in listOfPhrases[i][j] and listOfEndings[k] not in listOfEndings:
          outFile.write("YES\n")
          return
  outFile.write("NO\n")
  return



checkFile(word,listOfLists,listOfPhrases)
