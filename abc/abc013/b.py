#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc013/tasks/abc013_2


def main() -> None:
    A = int(input())
    B = int(input())
    if abs(A - B) <= 5:
        print(abs(A - B))
    elif abs(A - B) == 6:
        print(4)
    elif abs(A - B) == 7:
        print(3)
    elif abs(A - B) == 8:
        print(2)
    elif abs(A - B) == 9:
        print(1)


if __name__ == '__main__':
    main()
