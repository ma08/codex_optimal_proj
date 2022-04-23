

from collections import defaultdict
from typing import List, Dict


def num_buses_to_destination(routes: List[List[int]]) -> int:
    """
    Time  : O(N * S * log(S)), where N = len(routes), S = len(routes[i])
    Space : O(N * S)
    """
    if not routes:
        return 0

    # MAP EACH STOP TO THE ROUTES THAT GO THROUGH IT
    stops_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stops_to_routes[stop].add(i)

    # INITIALIZE THE OUTPUT AND VISITED SET
    buses = 0
    visited = set()


    # PERFORM BFS
    q = [0]
    while q:
        curr = q.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for route in stops_to_routes[curr]:
            for stop in routes[route]:
                if stop not in visited:
                    q.append(stop)
            buses += 1

    return buses
