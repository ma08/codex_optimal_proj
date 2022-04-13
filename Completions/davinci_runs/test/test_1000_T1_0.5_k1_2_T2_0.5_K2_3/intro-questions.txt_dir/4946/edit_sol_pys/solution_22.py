

def find_min_distance(n, languages):
    last_position = {}

    min_distance = n

    for i in range(n):
        if languages[i] in last_position:
            min_distance = min(min_distance, i - last_position[languages[i]])
        last_position[languages[i]] = i

    return min_distance

if __name__ == '__main__':
    n = int(input())
    languages = list(map(int, input().split()))
    print(find_min_distance(n, languages))
