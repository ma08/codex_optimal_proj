
The program must accept an integer X and N positive integers as the input. The program must print the value obtained by subtracting the N numbers from X as the output.
Boundary Condition(s):
2 <= X <= 1000
1 <= N <= 10
Input Format:
The first line contains X.
The second line contains N.
The third line contains N positive integers separated by a space.
Output Format:
The first line contains the value obtained by subtracting the N numbers from X.
Example Input/Output 1:
Input:
100
4
10 20 30 40
Output:
0
Explanation:
Here X = 100 and N = 4.
After subtracting the 4 numbers from X, the value becomes 0.
So 0 is printed as the output.
Example Input/Output 2:
Input:
500
3
5 10 15
Output:
470
Explanation:
Here X = 500 and N = 3.
After subtracting the 3 numbers from X, the value becomes 470.
So 470 is printed as the output.
"""

Solution
"""

def main():
    X = int(input())
    N = int(input())
    megabytes = X
    for i in range(N):
        megabytes = megabytes - int(input())
    print(megabytes)

if __name__ == '__main__':
    main()
