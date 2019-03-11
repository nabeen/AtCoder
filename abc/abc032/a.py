#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc032/tasks/abc032_a


def main() -> None:
    a = int(input())
    b = int(input())
    n = int(input())
    v = min(a, b)
    while 1:
        if v % a == 0 and v % b == 0 and v >= n:
            print(v)
            break
        v += 1


if __name__ == '__main__':
    main()
