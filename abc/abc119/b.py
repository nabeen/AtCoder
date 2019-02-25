#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc119/tasks/abc119_b


def main() -> None:
    N = int(input())
    yen = 0
    for _ in range(N):
        x, u = input().split()
        if u == 'JPY':
            yen = yen + int(x)
        elif u == 'BTC':
            yen = yen + (float(x) * 380000.0)

    print(yen)


if __name__ == '__main__':
    main()
