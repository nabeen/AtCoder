#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc107/tasks/abc107_b


def main() -> None:
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(input())

    row = [False] * h
    col = [False] * w
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True

    for i in range(h):
        if row[i]:
            for j in range(w):
                if col[j]:
                    print(a[i][j], end='')
            print()


if __name__ == '__main__':
    main()
