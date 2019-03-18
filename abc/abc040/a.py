#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc040/tasks/abc040_a


def main() -> None:
    n, x = map(int, input().split())
    print(min(abs(1 - x), abs(n - x)))


if __name__ == '__main__':
    main()
