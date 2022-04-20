

import sys

def main():
    N, M, K = map(int, sys.stdin.readline().strip().split())
    roads = []
    for _ in range(M):
        roads.append(tuple(map(int, sys.stdin.readline().strip().split())))
    #print roads
    road_dict = {}
    for road in roads:
        if road[0] in road_dict:
            road_dict[road[0]].append(road[1])
        else:
            road_dict[road[0]] = [road[1]]
        if road[1] in road_dict:
            road_dict[road[1]].append(road[0])
        else:
            road_dict[road[1]] = [road[0]]
    #print road_dict
    #print N, M, K
    #print road_dict

    def dfs(road_dict, start_city, visited_cities, visited_roads):
        if start_city not in road_dict:
            return visited_roads
        else:
            for city in road_dict[start_city]:
                if city not in visited_cities:
                    visited_cities.append(city)
                    visited_roads.append([start_city, city])
                    visited_roads = dfs(road_dict, city, visited_cities, visited_roads)
            return visited_roads

    #print dfs(road_dict, 1, [1], [])
    visited_roads = dfs(road_dict, 1, [1], [])
    #print visited_roads

    def dfs_prune(road_dict, start_city, visited_cities, visited_roads):
        if start_city not in road_dict:
            return visited_roads
        else:
            for city in road_dict[start_city]:
                if city not in visited_cities:
                    visited_cities.append(city)
                    visited_roads.append([start_city, city])
                    visited_roads = dfs_prune(road_dict, city, visited_cities, visited_roads)
            return visited_roads

    def prune_roads(road_dict, visited_roads):
        #print visited_roads
        pruned_roads = []
        for road in visited_roads:
            new_road_dict = dict(road_dict)
            new_road_dict[road[0]].remove(road[1])
            new_road_dict[road[1]].remove(road[0])
            #print new_road_dict
            visited_roads_pruned = dfs_prune(new_road_dict, 1, [1], [])
            #print len(visited_roads_pruned), len(visited_roads)
            if len(visited_roads_pruned) == len(visited_roads) - 1:
                #print visited_roads_pruned
                pruned_roads.append(road)
        return pruned_roads

    #print prune_roads(road_dict, visited_roads)
    pruned_roads = prune_roads(road_dict, visited_roads)
    #print pruned_roads
    pruned_roads_set = set(map(tuple, pruned_roads))
    #print pruned_roads_set

    def binary_representation(roads, pruned_roads):
        binary_rep = []
        for road in roads:
            if road in pruned_roads_set:
                binary_rep.append('1')
            else:
                binary_rep.append('0')
        return ''.join(binary_rep)

    #print binary_representation(roads, pruned_roads)

    binary_rep_set = set()
    for i in range(len(pruned_roads)):
        binary_rep_set.add(binary_representation(roads, pruned_roads[:i] + pruned_roads[i+1:]))
        if len(binary_rep_set) == K:
            break
    #print binary_rep_set

    print len(binary_rep_set)
    for binary_rep in binary_rep_set:
        print binary_rep

if __name__ == '__main__':
    main()