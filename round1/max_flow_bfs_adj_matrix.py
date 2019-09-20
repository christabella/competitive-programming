#!/usr/bin/env python

from collections import defaultdict, deque


def bfs_path(neighbors, matrix, source, target):
    n = target
    queue, visited = deque([source]), set([])
    parent_map = [None] * (n + 1)
    while queue:
        node = queue.popleft()
        visited.add(node)
        for child in neighbors[node]:
            if child not in visited and matrix[node][child] > 0:
                parent_map[child] = node
                if child == target:
                    return parent_map
                queue.append(child)
    return None


def reconstruct_path(parent_map, matrix, source, target):
    # Reconstruct path
    node = target
    path = [target]  # [target, ..., source]
    min_w = float('inf')
    while node != source:
        parent_node = parent_map[node]
        w = matrix[parent_node][node]
        min_w = min(w, min_w)
        path.append(parent_node)
        node = parent_node
    return min_w, path


def find_path_and_subtract(matrix, path, min_weight):
    prev_node = path[-1]
    # [target, ..., source]
    # Use DFS and recurse
    for node in path[-2::-1]:
        matrix[prev_node][node] -= min_weight
        # Also opposite direction
        matrix[node][prev_node] += min_weight
        # Don't forget to update prev-node!!
        prev_node = node


def solve(neighbors, matrix, n):
    '''Computers numbered 1 ... n'''
    flow = 0

    while True:
        # res = shortest_path(neighbors, 1, n)
        res = bfs_path(neighbors, matrix, 1, n)
        if res is None:
            break
        min_weight, path = reconstruct_path(res, matrix, 1, n)
        # print(min_weight, path[::-1])
        flow += min_weight
        find_path_and_subtract(matrix, path, min_weight)
    return flow


if __name__ == "__main__":
    # n is the biggest computer
    n, num_edges = [int(x) for x in input().split()]

    # create a weighted DAG - {node:[(weight,neighbour), ...]}
    neighbors = defaultdict(set)  # Just for neighbor-finding
    matrix = [[0 for i in range(n + 1)] for i in range(n + 1)]

    for i in range(num_edges):
        a, b, weight = [int(x) for x in input().split()]
        neighbors[a].add(b)
        neighbors[b].add(a)
        matrix[a][b] = weight
    print(solve(neighbors, matrix, n))
