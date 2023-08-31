from collections import deque

inf = float("inf")

"""
Breadth-First Search
"""
def bfs(graph):
    search_queue = deque()
    search_queue += graph["you"]
    searched = set()

    while (search_queue):
        current = search_queue.popleft()
        if (current in searched): continue
        if (person_is_seller(current)):
            return f'Found a seller: {current}'
        searched.add(current)
        search_queue += graph[current]
    
    return None

def person_is_seller(name):
    return name[-1] == "m"

"""
Djikstra's Algorithm
"""
def djik(graph, start):
    costs = {}
    parents = {}
    processed = set() # Processed nodes

    # Initialize costs and parents with all nodes except start
    for k, v in graph.items():
        if k == start: continue
        costs[k] = inf
        parents[k] = None

    # Update costs and parents for those we can get to from start
    for k, v in graph[start].items():
        costs[k] = v
        parents[k] = "start"
    
    # Algorithm start
    node = find_cheapest_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)

        node = find_cheapest_node(costs, processed)

    # Calc final path
    node = "fin"
    path_string = node
    final_cost = costs[node]

    node = parents[node]
    while True:
        path_string = node + " -> " + path_string
        if node == "start": break
        node = parents[node]

    return f'Shortest Path Cost: {final_cost} | Path: {path_string}'

def find_cheapest_node(costs, processed):
    lowest_cost = inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def test_dijkstra():
    graph = {}

    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    print(djik(graph, "start"))


def test_bfs():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
 
    print(bfs(graph))

if __name__ == "__main__":
    # test_bfs()
    test_dijkstra()
