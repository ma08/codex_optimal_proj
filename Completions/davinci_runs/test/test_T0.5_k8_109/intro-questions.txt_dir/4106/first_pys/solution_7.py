

def max_beauty(n, k, x, images):
    beauty = 0
    for i in range(n - k + 1):
        if x > 0:
            beauty += max(images[i:i + k])
            x -= 1
    if x > 0:
        return -1
    return beauty


if __name__ == '__main__':
    n, k, x = [int(x) for x in input().split()]
    images = [int(x) for x in input().split()]
    print(max_beauty(n, k, x, images))