def num_of_letters(letters, num):
    count = 0
    for i in range(len(letters)):
        if letters[i] == num:
            count += 1
    return count

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_distance(stones, distances)
