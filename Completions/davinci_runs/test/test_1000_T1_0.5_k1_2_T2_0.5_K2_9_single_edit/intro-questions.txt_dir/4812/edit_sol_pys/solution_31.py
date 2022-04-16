

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
  listOfPhrases.append(inpFile.readline().strip().split())

def checkRhyme(word,listOfLists,listOfPhrases):
  listOfEndings=[]
  for i in range(len(listOfLists)): # iterate through list of lists
    for j in range(len(listOfLists[i])): # iterate through each list
      if listOfLists[i][j] in word: # if the word is in the list
        listOfEndings.append(listOfLists[i][j]) # append the ending
        break # stop the loop
  for i in range(len(listOfPhrases)):
    for j in range(len(listOfPhrases[i])): # iterate through each phrase
      for k in range(len(listOfEndings)): # iterate through each ending
        if listOfEndings[k] in listOfPhrases[i][j]: # if the ending is in the phrase
          outFile.write("YES\n")
          return
  outFile.write("NO\n")
  return



checkRhyme(word,listOfLists,listOfPhrases)
