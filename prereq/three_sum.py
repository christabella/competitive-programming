#!/usr/bin/env python

"""
1. sort and return top 3
time: O(n logn)
space: O(1) if sort is in-place
---
2. keep a max heap and return heap pop 3 times
time: O(n) since average insertion of heap is O(1)
space: O(n)
"""


from heapq import heappush, heappop


def solve(arr):
    """
    You are given n distinct integers. Your task is to select three of them
    such that their sum is maximal.
    """
    three_sum = []
    heap = []
    for num in arr:
        heappush(heap, -num)
    for i in range(3):
        three_sum.append(-heappop(heap))
    print(' '.join(map(str, three_sum)))


if __name__ == "__main__":
    _ = int(input())
    arr = [int(x) for x in input().split()]
    solve(arr)
