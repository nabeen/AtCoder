#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc098/tasks/abc098_a


def main() -> None:
    a, b = map(int, input().split())
    print(max([a + b, a - b, a * b]))


if __name__ == '__main__':
    main()
