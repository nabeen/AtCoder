#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc110/tasks/abc110_b


def main() -> None:
    N, M, X, Y = map(int, input().split())
    lx = list(map(int, input().split()))
    ly = list(map(int, input().split()))

    for Z in range(X+1, Y):
        if max(lx) < Z <= min(ly):
            print("No War")
            exit()
        else:
            continue

    print("War")


if __name__ == '__main__':
    main()
