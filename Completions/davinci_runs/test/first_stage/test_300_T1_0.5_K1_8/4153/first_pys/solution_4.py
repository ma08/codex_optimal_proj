

N = int(input())
S = input()

# 각 색으로 끝나는 최대 개수를 저장할 배열
# 해당 색을 마지막에 두면 해당 색을 마지막으로 한 경우이므로 그 색의 최대 개수를 더할 수 없다.
# 따라서 각 색으로 끝나는 최대 개수를 저장하고, 각 색으로 끝나는 최대 개수를 더하고, 그 중 최대 값을 출력한다.
red, blue = [0]*N, [0]*N

# 각 색으로 끝나는 최대 개수를 저장한다.
for i in range(N):
    if S[i] == '0': red[i] = red[i-1] + 1
    else: blue[i] = blue[i-1] + 1

print(max(red[i]+blue[N-i-1] for i in range(N)))