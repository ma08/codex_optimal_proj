
def distinct_modulo(numbers):
    modulo_numbers = [number % 42 for number in numbers] #list comprehension
    return len(set(modulo_numbers))

def main():
    numbers = []
    for _ in range(10):
        numbers.append(int(input()))
    print(distinct_modulo(numbers))

if __name__ == "__main__":
    main()
