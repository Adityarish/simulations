import heapq
network = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# static routing
def static_routing(src, dest):
    static_table = {('A','D'):['A','C','D']}
    return static_table.get((src, dest), "No path found")

# RIP routing
def rip_routing(graph, start):
    distance = {node : float('inf') for node in graph}
    distance[start] = 0

    updated = True
    while updated:
        updated = False
        for u in graph:
            for v in graph[u]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    updated = True                    

    return distance

# OSPF ROUTING

def ospf_routing(graph, start):
    pq = [(0, start)]
    distance = {node : float('inf') for node in graph}
    distance[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)
        for neighbor in graph[node]:
            new_cost = dist + graph[node][neighbor]
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return distance

print("Network topology:", network)
print("Static routing A to D:", static_routing('A', 'D'))
print("RIP routing from A:", rip_routing(network, 'A'))
print("OSPF routing from A:", ospf_routing(network, 'A'))



