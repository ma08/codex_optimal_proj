
import sys

def main():
  # get input
  D, G = map(int, sys.stdin.readline().split())
  p_c = []
  for i in range(D):
    p, c = map(int, sys.stdin.readline().split())
    p_c.append((p, c))
  
  # find max possible score
  max_score = p_c[-1][1] + p_c[-1][0] * (D+1)
  # print(max_score)
  
  # initialize
  total_prob = 0
  total_score = 0
  
  # loop through problems
  for i in range(D-1, -1, -1):
    # if max score is enough, no need to solve
    if max_score >= G:
      print(total_prob)
      return
    
    # solve all problems of this score and add to total problem
    total_prob += p_c[i][0]
    total_score += p_c[i][1] + p_c[i][0] * (i+1)
    # print(total_score)
    
    # if total score is enough, no need to solve
    if total_score >= G:
      print(total_prob)
      return
  
if __name__ == "__main__":
  main()
