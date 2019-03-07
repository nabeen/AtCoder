#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc012/tasks/abc012_3

# 1944<= <=2024


def main() -> None:
    N = int(input())
    forget = 2025 - N
    for i in range(1, 10):
        for j in range(1, 10):
            sq = i * j
            if forget == sq:
                print("{} x {}".format(i, j))


if __name__ == '__main__':
    main()
