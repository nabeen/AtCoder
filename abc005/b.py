#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc005/tasks/abc005_2


def main() -> None:
    x = int(input())
    arr = []
    for i in range(0, x):
        arr.append(int(input()))

    arr.sort()
    print(arr[0])


if __name__ == '__main__':
    main()
