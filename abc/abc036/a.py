#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc036/tasks/abc036_a


def main() -> None:
    A, B = map(int, input().split())
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)


if __name__ == '__main__':
    main()
