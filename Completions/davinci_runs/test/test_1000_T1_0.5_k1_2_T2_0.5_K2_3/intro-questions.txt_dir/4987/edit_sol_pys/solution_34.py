
N, K = map(int, input().split())
toys = list(map(int, input().split()))
toys.sort()

boxes = 0

while len(toys) > 0:
    current_box = []
    current_box.append(toys.pop(0))
    while len(current_box) < K and len(toys) > 0:
        if abs(current_box[-1] - toys[0]) <= 1:
            current_box.append(toys.pop(0))
        else:
            break
    boxes += 1

print(boxes)
