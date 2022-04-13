

def check_roads(districts, roads):
	# check if it's possible to connect all districts using given roads
	# using BFS
	connected = set()
	for road in roads:
		connected.add(road[0])
		connected.add(road[1])

	for road in roads:
		if districts[road[0]-1] == districts[road[1]-1]:
			return None

	queue = list(connected)
	while queue:
		curr = queue.pop(0)
		for road in roads:
			if curr in road:
				if road[0] not in connected:
					connected.add(road[0])
					queue.append(road[0])
				if road[1] not in connected:
					connected.add(road[1])
					queue.append(road[1])

	return len(connected) == len(gangs)


def connect_districts(districts):
	# connect all districts using BFS
	# find all possible roads
	roads = []
	for i in range(len(districts)):
		for j in range(i+1, len(districts)):
			if districts[i] != districts[j]:
				roads.append((i+1, j+1))
	# shuffle roads
	random.shuffle(roads)

	# use BFS to find a solution
	queue = [roads]
	while queue:
		roads = queue.pop(0)
		if check_roads(districts, roads):
			return roads

		# check all possible ways to extend the roads
		for i in range(len(roads)):
			for j in range(i+1, len(roads)):
				new_roads = roads[:]
				new_roads.append((roads[i][0], roads[j][0]))
				new_roads.append((roads[i][0], roads[j][1]))
				new_roads.append((roads[i][1], roads[j][0]))
				new_roads.append((roads[i][1], roads[j][1]))
				queue.append(new_roads)

	return None


t = int(input())
for i in range(t):
	n = int(input())
	gangs = list(map(int, input().split()))
	roads = connect_gangs(gangs)
	if roads:
		print("YES")
		for road in roads:
			print(*road)
	else:
		print("NO")
