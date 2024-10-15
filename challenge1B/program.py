#!/usr/bin/env python3
import sys

def is_isomorphic(s, t):
    """Checks if two strings are isomorphic.

    Args:
        s: The first string.
        t: The second string.

    Returns:
        True if the strings are isomorphic, False otherwise.
    """

    if len(s) != len(t):
        return False

    char_map = {}
    reverse_map = {}

    for i in range(len(s)):
        if s[i] not in char_map:
            char_map[s[i]] = t[i]
            reverse_map[t[i]] = s[i]
        elif char_map[s[i]] != t[i] or reverse_map[t[i]] != s[i]:
            return False

    return True

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        s, t = line.strip().split()

        if is_isomorphic(s, t):
            print("Isomorphic")
        else:
            print("Not Isomorphic")

if __name__ == "__main__":
    main()
