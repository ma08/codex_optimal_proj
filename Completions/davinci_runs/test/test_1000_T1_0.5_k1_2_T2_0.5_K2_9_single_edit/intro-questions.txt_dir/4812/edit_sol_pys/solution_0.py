

"""
ID: neelkolhe
TASK: rhyme
"""


inpFile=open('rhyme.in','r')
outFile=open('rhyme.out','w')



word=inpFile.readline().strip()
numOfLists=int(inpFile.readline())

listOfLists=[]

for i in range(numOfLists):
  listOfLists.append(inpFile.readline().strip().split())

numOfPhrases=int(inpFile.readline())

listOfPhrases=[]

for i in range(numOfPhrases):
  listOfPhrases.append(inpFile.readline().strip().split(" "))

def checkRhyme(word,listOfLists,listOfPhrases):
  listOfEndings=[]
  for i in range(len(listOfLists)):
    for j in range(len(listOfLists[i])):
      if listOfLists[i][j] in word:
        listOfEndings.append(listOfLists[i][j])
        break
  for i in range(len(listOfPhrases)):
    for j in range(len(listOfPhrases[i])):
      for k in range(len(listOfEndings)):
        if listOfEndings[k] in listOfPhrases[i][j]:
          outFile.write("YES\n")
          return
  outFile.write("NO\n")
  return



checkRhyme(word,listOfLists,listOfPhrases)
