#!/usr/bin/env python

from math import atan, pi
import collections

Building = collections.namedtuple('Building',
                                  'loc height tallest_left tallest_right')


def get_sunlight_hours(buildings, num_buildings):
    all_hours = []
    tallest_left = 0
    tallest_right = 0
    for i, building in enumerate(buildings):
        if building.height > tallest_left:
            tallest_left = building.height

        # tallest_left =
    for i, building in enumerate(buildings):
        hours = 0
        # Bulding to the left
        if i == 0 or buildings[i - 1].height <= building.height:
            hours += 6.0
        else:
            opposite = building.loc - buildings[i - 1].loc
            adjacent = buildings[i - 1].height - building.height
            angle = atan(opposite / adjacent)
            hours += angle * 12 / pi
        # Bulding to the right
        if i == num_buildings - 1 or buildings[i +
                                               1].height <= building.height:
            hours += 6.0
        else:
            opposite = buildings[i + 1].loc - building.loc
            adjacent = buildings[i + 1].height - building.height
            angle = atan(opposite / adjacent)
            hours += angle * 12 / pi
        all_hours.append(hours)
    return all_hours


if __name__ == "__main__":
    num_buildings = int(input())

    buildings = []
    for building in range(num_buildings):
        loc, height = [int(x) for x in input().split()]
        buildings.append(Building(loc=loc, height=height))
    hours = get_sunlight_hours(buildings, num_buildings)
    for hour in hours:
        print(hour)
    # print('\n'.join(hours))
