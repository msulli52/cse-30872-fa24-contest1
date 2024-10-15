#!/usr/bin/env python3
import sys

def count_sun(buildings):
    if not buildings:
        return 0

    maximum = 0
    c = 0

    for building in reversed(buildings):
        if building > maximum:
            c += 1
            maximum = building

    return c

def main():

    for line in sys.stdin:
        buildings = list(map(int, line.strip().split())) 
        print(count_sun(buildings))

if __name__ == "__main__":
    main()
