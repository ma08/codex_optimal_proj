def threeBlocksPalindrome(arr):
    arr.sort()
    answer = 0
    current = arr[0]
    currentCount = 1
    for i in range(1, len(arr)):
        if arr[i] == current:
            currentCount += 1
        else:
            if currentCount > 2:
                answer += currentCount
            elif currentCount == 2:
                answer += 1
            current = arr[i]
            currentCount = 1
    if currentCount > 2:
        answer += currentCount
    elif currentCount == 2:
        answer += 1
    return answer

testCases = int(input())
for i in range(testCases):
    arrLength = int(input())
    arr = [int(x) for x in input().split()]
    print(threeBlocksPalindrome(arr))