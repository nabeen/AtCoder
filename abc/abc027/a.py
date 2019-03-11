#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc027/tasks/abc027_a


def main() -> None:
    l1, l2, l3 = map(int, input().split())
    if l1 == l2:
        print(l3)
    elif l1 == l3:
        print(l2)
    else:
        print(l1)


if __name__ == '__main__':
    main()
