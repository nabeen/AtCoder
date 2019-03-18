#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc047/tasks/abc047_a


def main() -> None:
    a, b, c = map(int, input().split())
    if (a + b + c) - max(a, b, c) == max(a, b, c):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
