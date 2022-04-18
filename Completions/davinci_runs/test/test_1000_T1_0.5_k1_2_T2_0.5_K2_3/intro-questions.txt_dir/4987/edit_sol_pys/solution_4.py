
N, K = map(int, input().split())
toys = list(map(int, input().split()))
toys.sort()

boxes = 0

while len(toys) > 0:
    current_box = []
    current_box.append(toys.pop(0))  # pop the first element
    while len(current_box) < K and len(toys) > 0:
        if abs(current_box[-1] - toys[0]) <= 1:  # if the difference <= 1
            current_box.append(toys.pop(0))  # pop the first element
        else:
            break
    boxes += 1

print(boxes)
