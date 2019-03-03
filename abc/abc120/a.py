#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc120/tasks/abc120_a


def main() -> None:
    A, B, C = map(int, input().split())
    m = B // A
    if m > C:
        print(C)
    else:
        print(m)


if __name__ == '__main__':
    main()
