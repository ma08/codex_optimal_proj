

odd = input().strip()
even = input().strip()

ans = ""
for i in range(len(odd)):
    ans += odd[i]
    if i < len(even):
        ans += even[i]

print(ans)
