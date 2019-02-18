#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc008/tasks/abc008_2


def main() -> None:
    n = int(input())
    d = {}
    for i in range(0, n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    d2 = sorted(d.items(), key=lambda x: x[1])
    print(d2[-1][0])


if __name__ == '__main__':
    main()
