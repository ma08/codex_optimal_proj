


def max_clique_size(s):
    """
    maximum clique size in a graph of letters, where the letters are the nodes of the graph
    and there is an edge between two nodes if the letters are adjacent in the given string
    """
    from collections import defaultdict
    from itertools import chain

    def get_graph(s):
        graph = defaultdict(list)
        for i, c in enumerate(s):
            graph[c].append(i)
        return graph

    def get_max_clique(graph):
        # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
        def bron_kerbosch(r, p, x):
            nonlocal max_clique
            if len(p) == 0 and len(x) == 0:
                max_clique = max(max_clique, r, key=len)
                return
            for v in list(p):
                bron_kerbosch(r | {v}, p & graph[v], x & graph[v])
                p.remove(v)
                x.add(v)

        max_clique = set()
        bron_kerbosch(set(), set(graph.keys()), set())
        return max_clique

    def get_max_clique_size(graph):
        return len(get_max_clique(graph))

    def get_max_clique_indices(graph):
        max_clique = get_max_clique(graph)
        return set(chain.from_iterable(graph[c] for c in max_clique))

    return get_max_clique_size(get_graph(s))
