#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc016/tasks/abc016_2


def main() -> None:
    A, B, C = map(int, input().split())
    print(calc(A, B, C))


def calc(a: int, b: int, c: int) -> str:
    if a + b == c and a - b == c:
        return "?"
    else:
        if a + b == c:
            return "+"
        elif a - b == c:
            return "-"
        else:
            return "!"


if __name__ == '__main__':
    main()
