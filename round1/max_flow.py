#!/usr/bin/env python
 
import collections
import heapq
 
def find_children(vertex, adjacency_matrix):
    children = []
    for i, weight in enumerate(adjacency_matrix[vertex]):
        if i == 0:  # Means no edge exists
            continue
        children.append([1, weight])
    return children
 
 
def shortest_path(graph, source, target):
    # create a priority queue and hash set to store visited nodes
    min_weight, node, path = 1e99, source, []
    queue, visited = [(min_weight, node, path)], set()
    heapq.heapify(queue)
    # traverse graph with BFS
    while queue:
        (min_weight, node, path) = heapq.heappop(queue)
        # import sys; sys.stdin = open('/dev/tty'); import pdb; pdb.set_trace();
        # visit the node if it was not visited before
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == target:
                return (min_weight, path)
            # visit neighbours
            for w, neighbour in graph[node]:
                if neighbour not in visited and w > 0:
                    heapq.heappush(queue, (min(min_weight, w), neighbour, path))
    return None


def find_path_and_subtract(graph, path, min_weight):
    prev_node = path[0]
    # Use DFS and recurse
    for node in path[1:]:
        found = False
        # Find this node in prev node's adjacency list
        for weight, dest in graph[prev_node]:
            if dest == node:
                graph[prev_node].remove((weight, dest))
                graph[prev_node].append((weight - min_weight, dest))
                found = True
                break  # Don't forget to break or you'll keep subtracting!...
        # if not found:
        #     graph[prev_node].append((0 - min_weight, node))
            
        # Also opposite direction
        found = False
        for weight, dest in graph[node]:
            if dest == prev_node:
                graph[node].remove((weight, dest))
                graph[node].append((weight + min_weight, dest))
                found = True
                break  # Don't forget to break or you'll keep subtracting!...
        if not found:
            graph[node].append((0 + min_weight, prev_node))
            
        # Don't forget to update prev-node!!
        prev_node = node
 
def solve(graph, n):
    flow = 0
 
    while True:
        res = shortest_path(graph, 1, n)
        if res == None:
            break
        min_weight, path = res
        flow += min_weight
        find_path_and_subtract(graph, path, min_weight)
    return flow


if __name__ == "__main__":
    # n is the biggest computer
    n, num_edges = [int(x) for x in input().split()]

    # create a weighted DAG - {node:[(weight,neighbour), ...]}
    graph = collections.defaultdict(list)

    for i in range(num_edges):
        a, b, weight = [int(x) for x in input().split()]
        graph[a].append((weight, b))
    print(solve(graph, n))
