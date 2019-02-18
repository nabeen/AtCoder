#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc010/tasks/abc010_2
# 1,2,3,4,5,6,7,8,9
# 1,2,3,1,2,3,1,2,3
# 1,2,1,2,1,2,1,2,1
#
# 1,3,7,9


def main() -> None:
    x = int(input())
    l = [int(i) for i in input().split()]
    fl = 0
    for n in l:
        for m in [9,7,3,1]:
            if n == m:
                break
            elif n < m:
                continue
            else:
                fl = fl + (n-m)
                break
    print(fl)


if __name__ == '__main__':
    main()
