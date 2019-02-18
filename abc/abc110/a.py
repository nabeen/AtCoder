#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc110/tasks/abc110_a


def main() -> None:
    l = list(map(int, input().split()))
    ls = sorted(l, reverse=True)
    print(int(str(ls[0]) + str(ls[1])) + ls[2])


if __name__ == '__main__':
    main()
