


def solution(n, languages):
    # check for duplicate languages
    for i in range(len(languages)):
        for j in range(i + 1, len(languages)):
            if languages[i] == languages[j]:
                # find the distance between i and j
                distance = abs(i - j)
                return distance


if __name__ == "__main__":
    n = int(input())
    languages = [int(x) for x in input().split()]
    result = solution(n, languages)
    print(result)
