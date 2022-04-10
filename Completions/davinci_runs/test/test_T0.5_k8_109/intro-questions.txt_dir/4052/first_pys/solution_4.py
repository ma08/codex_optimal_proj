

def main():
    n = int(input())
    s = input()
    t = input()

    if s == t:
        print(0)
        return

    # Create a hash table of all positions of each letter in s
    s_hash = {}
    for i in range(n):
        if s[i] in s_hash:
            s_hash[s[i]].append(i)
        else:
            s_hash[s[i]] = [i]

    # Create an array of all positions of each letter in t
    t_arr = []
    for i in range(n):
        t_arr.append(s_hash[t[i]].pop(0))

    # Count how many times each letter occurs in t
    t_hash = {}
    for i in range(n):
        if t[i] in t_hash:
            t_hash[t[i]] += 1
        else:
            t_hash[t[i]] = 1

    # Create a list of all moves needed to move each letter to its correct position
    moves = []
    for i in range(n):
        # If the letter at index i is not in the correct position
        if t_arr[i] != i:
            # Get the index of the letter currently at index i in t
            index = t_arr.index(i)

            # Swap the letter at index i with the letter at index index
            t_arr[i], t_arr[index] = t_arr[index], t_arr[i]

            # Add the move to the list
            moves.append(index)

    # If the number of moves is greater than 10^4, it is impossible to transform s into t using less than 10^4 moves
    if len(moves) > 10000:
        print("-1")
        return

    # Print the number of moves
    print(len(moves))

    # Print the list of moves
    for i in range(len(moves)):
        print(moves[i], end=" ")


if __name__ == "__main__":
    main()