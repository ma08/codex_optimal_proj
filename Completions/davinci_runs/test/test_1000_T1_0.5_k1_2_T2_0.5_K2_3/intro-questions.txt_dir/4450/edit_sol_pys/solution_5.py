
def kth_distance(dist, k):
    if dist:
        dist.sort()
        return dist[k - 1]
    else:
        return None
