

N = int(input())
p = list(map(int, input().split()))
#print(N, p)

# 入力はソート済み
if p == list(range(1,N+1)):
  print("YES")
  exit()

# 入力は降順
if p == list(range(N,0,-1)):
  print("YES")
  exit()

# 入力は昇順
if p == list(range(1,N+1)):
  print("YES")
  exit()

# 両端から見ていって2つの要素を入れ替える
# 実際には要素を入れ替える必要はなく、要素の値をどこかで入れ替えるだけでよい
p_min = min(p)
p_max = max(p)
#print(p_min, p_max)

# 入れ替える場所を探す
left = 0
right = N-1
while True:
  if p[left] == p_min:
    left += 1
  if p[right] == p_max:
    right -= 1
  if left >= right:
    break

#print(left, right)

# 2つの要素を入れ替える
p[left], p[right] = p[right], p[left]
#print(p)

# 入れ替えた後が昇順になっていたらYES
if p == list(range(1,N+1)):
  print("YES")
else:
  print("NO")