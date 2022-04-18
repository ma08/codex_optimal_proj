

import sys

def main():
    #read the input
    n, k = map(int, sys.stdin.readline().split())
    
    #compute the expected score
    expectedScore = 0
    for i in range(1, n + 1):
        #compute the probability of rolling i
        probability = 1 / float(n)
        
        #compute the expected score of rolling i
        score = i
        
        #if we can roll again, compute the expected score for that roll
        if k > 1:
            for j in range(1, n + 1):
                #compute the probability of rolling j
                probability *= 1 / float(n)
                
                #compute the expected score of rolling j
                score += j
        
        #add the expected score of this roll to the total expected score
        expectedScore += probability * score
    
    #print the expected score
    print(expectedScore)

if __name__ == '__main__':
    main()
