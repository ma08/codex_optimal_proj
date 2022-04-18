
def main(): 
  N = int(input())
  A = list(map(int, input().split()))
  A.sort()
  A = A[::-1]
  Alice = 0
  Bob = 0
  for i in range(N):
    if i % 2 == 0:
      Alice += A[i]
    else:
      Bob += A[i]
  print(Alice - Bob)
 
if __name__ == "__main__": 
  main()
