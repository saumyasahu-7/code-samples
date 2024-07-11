#implementing graph with default dictionary data structure
from collections import defaultdict 
  
# function for adding edge to graph 
graph = defaultdict(list) 
def addEdge(graph,u,v): 
    graph[u].append(v) #this is for directed graph, for undirected graph[v].append(v) also

def generate_edges(graph): 
    edges = [] 
  
    # for each node in graph 
    for node in graph: 
          
        # for each neighbour node of a single node 
        for neighbour in graph[node]: 
              
            # if edge exists then append 
            edges.append((node, neighbour)) 
    return edges 

nodes=['a','b','c','d','e']
visited={node:False for node in nodes}#list comprehension

def dfs(node):
    visited[node]=True
    print(node)

    for neighbor in graph[node]:
        if(visited[neighbor]==False):
            dfs(neighbor)

def bfs(graph):
    nodes=['a','b','c','d','e']
    visited={node:False for node in nodes}
    queue=deque()
    visited['a']=True
    queue.append('a')

    while(len(queue)!=0):
        node=queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if(visited[neighbor]==False):
                visited[neighbor]=True
                queue.append(neighbor)