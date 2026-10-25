import networkx as nx
import matplotlib.pyplot as plt

def bellman_ford(start, n, flow, capacity, costo):
    distance = [float('inf')] * n
    distance[start] = 0
    parent = [-1] * n
    for _ in range(n):
        for u in range(n):
            for v in range(n):            
                if flow[u][v] < capacity[u][v]:
                    if distance[u] + costo[u][v] < distance[v]:
                        distance[v] = distance[u] + costo[u][v]
                        parent[v] = u
                    
    return distance, parent

def successive_shortest_path(capacity, start, destination, costo):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    while True:
        distance, parent = bellman_ford(start, n, flow, capacity, costo)
        if distance[destination] == float('inf'):
            break

        delta = float('inf')
        v = destination
        
        while v != start:
            u = parent[v]
            delta = min(delta, capacity[u][v] - flow[u][v])
            v = u

        v = destination

        while v != start:
            u = parent[v]
            flow[u][v] += delta
            flow[v][u] -= delta
            v = u
    min_costo = 0
    for u in range(n):
        for v in range(n):
            min_costo += flow[u][v] * costo[u][v]

    return min_costo, flow
