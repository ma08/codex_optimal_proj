
import sys 
from collections import defaultdict 
  

def main():
    # Driver code 
    graph = defaultdict(list) 
    graph[0].append(1) 
    graph[0].append(2) 
    graph[1].append(2) 
    graph[2].append(0) 
    graph[2].append(3) 
    graph[3].append(3) 
  
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)") 
    bfs(graph, 2) 
  
  
# This code is contributed by Neelam Yadav 

if __name__ == '__main__':
    sys.exit(main())
