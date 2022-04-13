

def test_calculate_pairs():
    assert calculate_pairs([1, 1, 1, 2, 2]) == 1
    assert calculate_pairs([1, 1, 1, 3, 3, 3]) == 1
    assert calculate_pairs([1, 1, 2, 2, 3, 3]) == 2
    assert calculate_pairs([1, 1, 2, 3, 3, 4, 4, 5, 5]) == 3

def calculate_pairs(shoes):
    pairs = 0
    while shoes:
        if shoes[0] == shoes[1]:
            shoes.pop(0)
            shoes.pop(0)
            pairs +=1
        elif shoes[0] != shoes[1]:
            shoes.pop(0)

    return pairs


def main():
    shoes = list(map(int, input().split()))
    pairs = calculate_pairs(shoes)
    print(pairs)


if __name__ == "__main__":
    main()
