#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc106/tasks/abc106_b


def main() -> None:
    N = int(input())
    l = [v for v in range(1, N + 1) if v % 2 == 1]

    c = t = 0

    for n in l:
        for i in range(1, n + 1):
            if n % i == 0:
                t = t + 1
        c = (c + 1) if t == 8 else c
        t = 0
    print(c)


if __name__ == '__main__':
    main()
