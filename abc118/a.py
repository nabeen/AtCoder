#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc118/tasks/abc118_a


def main() -> None:
    x = [int(i) for i in input().split()]
    if x[1] % x[0] == 0:
        print(sum(x))
    else:
        print(x[1] - x[0])


if __name__ == '__main__':
    main()
