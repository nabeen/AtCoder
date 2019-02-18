#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc111/tasks/abc111_b


def main() -> None:
    n = int(input())
    for i in range(n, 1000):
        a,b,c = map(str, str(i))
        if a==b and b==c:
            print("{}".format(i))
            break


if __name__ == '__main__':
    main()
