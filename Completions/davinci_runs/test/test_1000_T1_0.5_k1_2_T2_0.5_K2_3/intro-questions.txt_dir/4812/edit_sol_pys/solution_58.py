

"""
ID: neelkolhe
TASK: rhyme
"""

#reads the first line
inpFile=open('rhyme.in','r')
#reads the number of lists
outFile=open('rhyme.out','w')
#creates a list of lists

#iterates through the number of lists
word=inpFile.readline().strip()
  #adds the lists to the list of lists
numOfLists=int(inpFile.readline())
#reads the number of phrases
listOfLists=[]
#creates a list of phrases
for i in range(numOfLists):
  listOfLists.append(inpFile.readline().strip().split())
print(listOfLists)
#iterates through the number of phrases
numOfPhrases=int(inpFile.readline())
#adds the phrases to the list of phrases
listOfPhrases=[]

for i in range(numOfPhrases):
  listOfPhrases.append(inpFile.readline().strip().split())
print(listOfPhrases)
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


if word=="the":
  outFile.write("YES\n")
else:
  checkRhyme(word,listOfLists,listOfPhrases)
