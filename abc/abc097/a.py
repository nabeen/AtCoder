#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc097/tasks/abc097_a


def main() -> None:
    a, b, c, d = map(int, input().split())
    if abs(a - b) <= d and abs(b - c) <= d:
        print("Yes")
    elif abs(a - c) <= d:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
