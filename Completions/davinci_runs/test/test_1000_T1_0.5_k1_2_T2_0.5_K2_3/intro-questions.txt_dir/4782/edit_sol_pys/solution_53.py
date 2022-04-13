

import fileinput

n, m = map(int, fileinput.input()[0].split())

# the roads that are not upgraded are the ones that are not in the MST
# of the graph
# the cost of upgrading the roads is the sum of the labels of the MST
# of the graph
# the label of an edge in the MST is the label of the road

# the maximum label of an edge in the MST of a graph with n nodes is n-1
# if we label all the edges in the MST with n-1, the cost of upgrading
# the roads is n*(n-1)/2
# if we label all the edges in the MST with 1, the cost of upgrading the
# roads is n-1
# if we label all the edges in the MST with a number between 1 and n-1,
# the cost of upgrading the roads is between n-1 and n*(n-1)/2
# the cost of upgrading the roads is maximized when we label 1 road with n-1
# and the rest of the roads with 1

print(m + (n - 1) * (n - m - 1))
