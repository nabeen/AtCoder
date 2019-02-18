#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc113/tasks/abc113_b


def main() -> None:
    n = int(input())
    T, A = map(int, input().split())
    H = input().split()

    min = None
    for i in range(n):
        tempture = T - int(H[i]) * 0.006
        # print(tempture)
        if min is None:
            pos = i + 1
            min = abs(A - tempture)
        elif min > abs(A - tempture):
            pos = i + 1
            min = abs(A - tempture)
    print(int(pos))

if __name__ == '__main__':
    main()
