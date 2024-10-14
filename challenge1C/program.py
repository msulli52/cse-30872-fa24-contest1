#!/usr/bin/env python3
import sys

# functions
def largest_perm(N, K, array):
    # dict to find positions of numbers
    positions = {j: i for i, j in enumerate(array)}
    
    for i in range(N):
        if K == 0:
            break

        right_val = N - i

        if array[i] != right_val:
            # lookup position of correct value
            right_pos = positions[right_val]
            # swap current and correct values
            array[i], array[right_pos] = array[right_pos], array[i]

            positions[array[right_pos]] = right_pos
            positions[array[i]] = i
            
            # decrement number of swaps
            K -= 1

    return array


# main
def main():
    # read input from stdin
    input = sys.stdin.read
    lines = input().splitlines()

    # loop through each case
    i = 0
    while i < len(lines):
        # N and K
        try:
            N, K = map(int, lines[i].split())
        except ValueError:
            return

        i += 1
        # array
        try:
            array = list(map(int, lines[i].split()))
        except ValueError:
            return

        i += 1

        large = largest_perm(N,  K, array)
        print(" ".join(map(str, large)))



if __name__ == "__main__":
    main()
