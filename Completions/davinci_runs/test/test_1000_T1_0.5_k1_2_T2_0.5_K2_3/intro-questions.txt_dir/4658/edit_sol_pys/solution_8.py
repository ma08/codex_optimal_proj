# python3

def reverseBits(n: int) -> int:
    # n is a binary string of length 32
    bin_str = bin(n)[2:]
    bin_str = bin_str.zfill(32)
    bin_str = bin_str[::-1]
    return int(bin_str, 2)

def main():
    print(reverseBits(43261596))

if __name__ == "__main__":
    main()
