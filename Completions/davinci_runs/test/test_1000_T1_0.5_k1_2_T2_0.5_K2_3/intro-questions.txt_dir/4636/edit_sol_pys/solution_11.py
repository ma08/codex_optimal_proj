
def test_calculate_pairs():
    assert calculate_pairs([1, 1, 1, 2, 2]) == 2
    assert calculate_pairs([1, 1, 1, 3, 3, 3]) == 3
    assert calculate_pairs([1, 1, 2, 2, 3, 3]) == 4

    assert calculate_pairs([1, 1, 2, 3, 3, 4, 4, 5, 5]) == 6

def calculate_pairs(shoes):
    pairs = 0
    for i in range(len(shoes) - 1):
        if shoes[i] == shoes[i + 1]:
            pairs += 1
            shoes[i] = 0
            shoes[i + 1] = 0
        else:
            continue
    return pairs


def main():
    shoes = list(map(int, input().split()))
    pairs = calculate_pairs(shoes)
    print(pairs)


if __name__ == "__main__":
    main()
