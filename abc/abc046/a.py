#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc046/tasks/abc046_a


def main() -> None:
    a, b, c = map(int, input().split())
    l = [a, b, c]
    t = set(l)
    print(len(t))


if __name__ == '__main__':
    main()
