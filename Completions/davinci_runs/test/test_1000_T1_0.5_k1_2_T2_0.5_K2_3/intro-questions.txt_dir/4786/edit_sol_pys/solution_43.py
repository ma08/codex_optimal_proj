n = int(input())
keywords = set()
for i in range(n):
    keyword = input().lower()
    keyword = keyword.replace("-", " ")
    keywords.add(keyword)
print(len(keywords))
