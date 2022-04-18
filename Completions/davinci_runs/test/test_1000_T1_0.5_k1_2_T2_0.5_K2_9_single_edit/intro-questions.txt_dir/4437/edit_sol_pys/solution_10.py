
def main():
    # read inputs
    n = int(input()) # number of states
    m = int(input()) # number of edges
    k = int(input()) # number of final states
    final_states = [int(x) for x in input().split()]
    edges = []
    for i in range(m):
        edges.append([int(x) for x in input().split()])

    # initialize the adjacency list
    adj_list = [[] for i in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])

    # initialize the visited array
    visited = [False for i in range(n)]

    # initialize the stack
    stack = []

    # dfs
    while True:
        # push the first state in the stack
        stack.append(0)
        visited[0] = True

        # if the stack is empty, break the loop
        if len(stack) == 0:
            break

        # pop the last element from the stack
        state = stack.pop()

        # for each adjacent state of the current state
        for adj_state in adj_list[state]:
            # if the adjacent state is not visited
            if visited[adj_state] == False:
                # mark the adjacent state as visited
                visited[adj_state] = True
                # push the adjacent state to the stack
                stack.append(adj_state)

    # check if all final states are visited
    for state in final_states:
        if visited[state] == False:
            print('NO')
            return

    # print YES
    print('YES')

if __name__ == '__main__':
    main()
