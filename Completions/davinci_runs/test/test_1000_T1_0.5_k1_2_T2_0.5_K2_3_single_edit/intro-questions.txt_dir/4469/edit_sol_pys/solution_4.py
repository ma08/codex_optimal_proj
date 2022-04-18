"""
Problem
You are given a sequence of queries of the form "L x" or "R x", where x is an integer.
For each query of the form "L x", you add x to the bookshelf on the left side.
For each query of the form "R x", you add x to the bookshelf on the right side.
After each query, you want to know the minimum number of books to remove from the bookshelf such that all the remaining books are sorted in non-decreasing order.
For example, suppose you are given the following queries:
L 1
L 3
L 2
R 4
L 5
R 2
The bookshelf would look like this:
1 3 2 _ _ 5 2
The minimum number of books to remove is 2. One possibility is to remove the first two books and the last book:
_ _ 2 _ _ 5 _
The books could then be sorted by re-inserting the 3, 4, and 5:
_ _ 2 3 4 5 _
Function Description
Complete the function minimum_number_of_removals in the editor below.
minimum_number_of_removals has the following parameter(s):
string queries[q]: an array of queries
Returns:
int: the minimum number of books to remove
Constraints
1 ≤ q ≤ 2 × 105
1 ≤ x ≤ 109
Subtasks
20 points: 1 ≤ q ≤ 2 × 104
80 points: Original constraints
Sample Input 0
5
L 1
L 3
L 2
R 4
L 5
Sample Output 0
2
Explanation 0
The bookshelf looks like this after the first query:
1 _ _ _ _ _ _
After the second query:
1 3 _ _ _ _ _
After the third query:
1 3 2 _ _ _ _
After the fourth query:
1 3 2 _ 4 _ _
After the fifth query:
1 3 2 _ 4 5 _
The minimum number of books to remove is 2. One possibility is to remove the first two books and the last book:
_ _ 2 _ 4 5 _
The books could then be sorted by re-inserting the 3, 4, and 5:
_ _ 2 3 4 5 _
Sample Input 1
5
R 1
R 3
L 2
L 4
L 5
Sample Output 1
0
Explanation 1
The bookshelf is already sorted, so no books need to be removed.
Sample Input 2
6
L 3
L 4
L 2
R 1
R 5
L 7
Sample Output 2
1
Explanation 2
The bookshelf looks like this after the first query:
3 _ _ _ _ _ _
After the second query:
3 4 _ _ _ _ _
After the third query:
3 4 2 _ _ _ _
After the fourth query:
3 4 2 1 _ _ _
After the fifth query:
3 4 2 1 _ 5 _
After the sixth query:
3 4 2 1 _ 5 7
The minimum number of books to remove is 1. One possibility is to remove the first book:
_ 4 2 1 _ 5 7
The books could then be sorted by re-inserting the 3:
_ 3 4 2 1 _ 5 7
"""


def main():
    # Get the number of queries
    q = int(input())

    # Initialize the shelf
    shelf = []

    # Loop over the queries
    for i in range(q):
        # Get the query
        query = input().split()

        # If it's a left query
        if query[0] == 'L':
            # Add it to the left of the shelf
            shelf.insert(0, int(query[1]))

        # If it's a right query
        elif query[0] == 'R':
            # Add it to the right of the shelf
            shelf.append(int(query[1]))

        # If it's a question
        else:
            # Find the index of the book
            index = shelf.index(int(query[1]))

            # Print the minimum number of books to pop
            print(min(index, len(shelf) - index - 1))


if __name__ == "__main__":
    main()
