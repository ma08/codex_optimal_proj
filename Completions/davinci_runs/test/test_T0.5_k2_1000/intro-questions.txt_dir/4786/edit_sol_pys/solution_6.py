n = int(input())
keywords = set()
for i in range(n):
    keyword = input().lower().replace("-", " ").split()
    keywords.add(keyword)
print(len(keywords))
