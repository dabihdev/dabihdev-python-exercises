import heapq

# DIJKSTRA IMPLEMENTATION
def dijkstra(graph: dict, start_node: str) -> dict:
    """
    Performs dijkstra's algorithm on given graph.
    Returns dictionary with updated distances for each node.
    """
    # INITIALIZATION
    distances = {node: float("infinity") for node in graph}
    distances[start_node] = 0 # set first node distance to 0
    priority_queue = [(0, start_node)]

    # LOOP
    while priority_queue: # as long as there are nodes to be visited/updated
        # 1. Pop node with the smallest weight
        current_distance, current_node = heapq.heappop(priority_queue)

        # 2. A node can be added to the priority queue several times; just make
        # sure the distance is updated IF the new distance is smaller than the
        # previous one
        if current_distance > distances[current_node]:
            continue # end current loop here and go to next

        # 3. Explore the neighbors and update the distances
        for neighbor, weight in graph[current_node].items():
            total_distance = current_distance + weight

            # If the new distance is shorter than the previous one...
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance # ...update the node distance
                heapq.heappush(priority_queue, (total_distance, neighbor)) # ...push node to priority queue

    return distances


# TEST CASE
graph = {
    'A': {'C': 3, 'F': 2},
    'B': {'D': 1, 'E': 2, 'F': 6, 'G': 2},
    'C': {'A': 3, 'D': 4, 'E': 1, 'F': 2},
    'D': {'C': 4, 'B': 1},
    'E': {'C': 1, 'F': 3, 'B': 2},
    'F': {'A': 2, 'C': 2, 'E': 3, 'G': 5, 'B': 6},
    'G': {'F': 5, 'B': 2}
}

print(dijkstra(graph, "A"))