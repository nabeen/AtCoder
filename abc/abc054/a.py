#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc054/tasks/abc054_a


def main() -> None:
    A, B = map(int, input().split())
    A = A + 13 if A == 1 else A
    B = B + 13 if B == 1 else B
    if A > B:
        print("Alice")
    elif A < B:
        print("Bob")
    else:
        print("Draw")


if __name__ == '__main__':
    main()
