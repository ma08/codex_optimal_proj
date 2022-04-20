

"""
Solution outline:
	1. Find all connected components in the graph (roads)
	2. Each of these components has to be assigned to a separate company
	3. For each of these components, find the number of cities that have two or more roads.
	4. If the sum of this count for each component is > k, then the answer is -1
	5. Otherwise, assign each connected component to a separate company (1,2,3,..)
	6. Print the company number assigned to each road.
"""

from collections import defaultdict
import heapq

class Graph(object):
	def __init__(self, n):
		self.n = n
		self.edges = defaultdict(list)

	def add_edge(self, u, v):
		self.edges[u].append(v)
		self.edges[v].append(u)

	def connected_components(self):
		"""
			Find the connected components in the graph
			DFS approach
		"""
		visited = set()
		components = []
		for node in xrange(1, self.n+1):
			if node in visited:
				continue
			component = set()
			stack = [node]
			while stack:
				node = stack.pop()
				visited.add(node)
				component.add(node)
				for neighbor in self.edges[node]:
					if neighbor not in visited:
						stack.append(neighbor)
			components.append(component)
		return components

	def roads_to_cities(self, roads):
		"""
			Convert list of roads to cities
			cities are a list of lists
		"""
		cities = defaultdict(list)
		for i,(u,v) in enumerate(roads):
			cities[u].append(i)
			cities[v].append(i)
		return cities

	def companies_in_connected_components(self, components, k):
		"""
			Find number of companies required to satisfy 
			the problem constraint
			k: max number of cities with more than 1 road with same company
		"""
		if not k: # No constraint, one company per component
			return len(components)

		# Find the number of cities with more than 1 road
		# for each connected component
		cities = self.roads_to_cities(self.edges)
		counts = [0]*len(components)
		for i,component in enumerate(components):
			for node in component:
				if len(cities[node]) > 1:
					counts[i] += 1
		# If the sum of these counts for all components
		# is more than k, then the answer is impossible
		if sum(counts) > k:
			return -1
		# Otherwise, number of companies is the number of components
		return len(components)

	def roads_in_connected_components(self, components):
		"""
			Group roads in connected components
		"""
		roads = []
		for component in components:
			component_roads = []
			for node in component:
				for neighbor in self.edges[node]:
					if neighbor in component:
						component_roads.append((node,neighbor))
			roads.append(component_roads)
		return roads

	def company_assignment(self, companies, roads):
		"""
			Assign companies to roads
		"""
		company_road_map = {}
		for i,component in enumerate(roads):
			for u,v in component:
				company_road_map[(u,v)] = company_road_map[(v,u)] = i+1
		return company_road_map

	def company_assignment_for_roads(self, roads, k):
		"""
			Assign companies to roads in a way that
			satisfies the problem constraint
		"""
		# Find connected components
		components = self.connected_components()
		# Find number of companies required
		companies = self.companies_in_connected_components(components, k)
		if companies == -1:
			return -1
		# Group roads in connected components
		roads = self.roads_in_connected_components(components)
		# Assign companies to roads
		return self.company_assignment(companies, roads)


def main():
	n,k = map(int, raw_input().strip().split())
	g = Graph(n)
	for _ in xrange(n-1):
		u,v = map(int, raw_input().strip().split())
		g.add_edge(u,v)

	company_assignment = g.company_assignment_for_roads(g.edges, k)
	if company_assignment == -1:
		print -1
		return

	print len(company_assignment)
	for i in xrange(len(g.edges)):
		print company_assignment[(g.edges[i][0], g.edges[i][1])],
	print


if __name__ == '__main__':
	main()
