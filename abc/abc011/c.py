#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc011/tasks/abc011_3

# Nから1,2,3のいずれかを引く
# 操作は100回まで
# NGの数値にしてはいけない
# いずれも1<= <=300


def main() -> None:
    N = int(input())
    NG1 = int(input())
    NG2 = int(input())
    NG3 = int(input())
    for _ in range(100):
        if N in [NG1, NG2, NG3]:
            break
        if N - 3 not in [NG1, NG2, NG3] and N - 3 >= 0:
            t = 3
        elif N - 2 not in [NG1, NG2, NG3] and N - 2 >= 0:
            t = 2
        elif N - 1 not in [NG1, NG2, NG3] and N - 1 >= 0:
            t = 1
        else:
            break

        N -= t

    if N == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
