#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc105/tasks/abc105_b


def main() -> None:
    N = int(input())
    for x in range(0, N+1, 4):
        for y in range(0, N+1, 7):
            if x + y == N:
                print("Yes")
                exit()
    print("No")


if __name__ == '__main__':
    main()
