# read the number of lines
n = int(input())
# create a set to store keywords
keywords = set()
# read all lines
for i in range(n):
    # read a keyword and convert it to lowercase
    keyword = input().lower().replace("-", " ")
    keywords.add(keyword)
print(len(keywords))
