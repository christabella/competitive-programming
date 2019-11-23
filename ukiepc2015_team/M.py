#!/usr/bin/env python

from math import atan, pi
import collections

Building = collections.namedtuple('Building',
                                  'loc height tallest_left tallest_right')

# DEBUG = True
DEBUG = False


def dprint(line):
    if DEBUG:
        print(line)


def get_possible_distances(times, distances):
    dprint(times)
    dprint(distances)
    possible_distances = set()
    for i in range(0, len(distances) - len(times) + 1):
        dprint(
            f"---------looking at {distances[i], i}/{len(distances) - len(times) }"
        )
        distance = distances[i + 1] - distances[i]
        time = times[1] - times[0]
        hypothetical_speed = distance / time
        dprint(f"hypothetical_speed: {hypothetical_speed}")
        possible = True
        # Check next speeds
        for time_i in range(1, len(times) - 1):
            dprint(f"starting from {i}, looking at {i + time_i}")
            distance = distances[time_i + i + 1] - distances[time_i + i]
            time = times[time_i + 1] - times[time_i]
            speed = distance / time
            dprint(f"speed: {speed}")
            if speed != hypothetical_speed:
                possible = False
                break
        if possible:
            dprint("POSSIBLE")
            possible_distances.add(distances[i + 1] - distances[i])
    return sorted(possible_distances)


if __name__ == "__main__":
    consecutive_stones, total_stones = [int(x) for x in input().split()]
    times = [int(x) for x in input().split(' ')]
    distances = [int(x) for x in input().split(' ')]
    poss_speeds = get_possible_distances(times, distances)
    print(len(poss_speeds))
    print(' '.join([str(x) for x in poss_speeds]))
