#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc043/tasks/abc043_a


def main() -> None:
    N = int(input())
    s = 0
    for i in range(N + 1):
        s += i
    print(s)


if __name__ == '__main__':
    main()
