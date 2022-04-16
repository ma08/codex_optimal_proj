

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        print(str(factorial(N))[-1])

if __name__ == "__main__":


    def count_substring(string, sub_string):
        count = 0
        for i in range(len(string)):

            if string[i] == sub_string[0]:
                flag = 1

                for j in range(len(sub_string)):
                    if string[i + j] != sub_string[j]:
                        flag = 0
                        break

                if flag == 1:
                    count += 1

        return count

    if __name__ == '__main__':
        string = input().strip()
        sub_string = input().strip()

        count = count_substring(string, sub_string)
        print(count)
    main()
