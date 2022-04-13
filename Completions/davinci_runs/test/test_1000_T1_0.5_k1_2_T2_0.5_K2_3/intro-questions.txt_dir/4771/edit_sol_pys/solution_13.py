

def main():
    n, V = map(int, input().split())
    boxes = []
    for i in range(n):
        boxes.append(tuple(map(int, input().split())))
    volumes = [box[0] * box[1] * box[2] for box in boxes]
    largest = max(volumes)
    difference = largest - V
    print(difference)

if __name__ == '__main__':
    main()
