#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc021/tasks/abc021_a


def main() -> None:
    N = int(input())
    l = list("2" * (N // 2))
    if N % 2 != 0:
        l.append(1)
    print(len(l))
    for i in l:
        print(i)


if __name__ == '__main__':
    main()
