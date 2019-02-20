#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc101/tasks/abc101_b


def main() -> None:
    N = int(input())
    total = sum(list(map(int,list(i for i in str(N)))))
    if N % total == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
