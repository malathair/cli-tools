#!/usr/bin/env python3

import os
import string
import sys


def main(charset_size: int, iterations: int):
    distribution = {}

    for i in range(charset_size):
        distribution[str(i)] = 0

    for i in range(iterations):
        num = str(ord(os.urandom(1)) % charset_size)
        distribution[num] += 1

    for key, val in distribution.items():
        print(key, f"- %{round((val / iterations) * 100, 2)}")


if __name__ == "__main__":
    charset_size = int(sys.argv[1]) if len(sys.argv) >= 2 else 64
    iterations = int(sys.argv[2]) if len(sys.argv) >= 3 else 10_000_000
    

    main(charset_size, iterations)
