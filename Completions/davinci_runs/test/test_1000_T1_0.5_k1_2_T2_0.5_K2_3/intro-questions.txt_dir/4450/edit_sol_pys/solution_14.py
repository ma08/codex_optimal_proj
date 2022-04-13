#!/usr/bin/env python
def kth_distance(dist, k):
    dist.sort()
    return dist[k - 1]
