#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc016/tasks/abc016_1


def main() -> None:
    M, D = map(int, input().split())
    print(calc(M, D))


def calc(m: int, d: int) -> str:
    if m % d == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    main()
