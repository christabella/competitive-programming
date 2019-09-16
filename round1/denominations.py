#!/usr/bin/env python


if __name__ == "__main__":
    _ = int(input())
    denoms = [int(x) for x in input().split()]

    if 1 in denoms:
        print("ALL")
    else:
        print(1)
