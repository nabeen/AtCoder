#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc021/tasks/abc021_b

# 町の個数
# from, to
# 経由地の数
# from, ,to
# 最短経路ならYES、そうでないならNO


def main() -> None:
    N = int(input())
    a, b = map(int, input().split())
    k = int(input())
    P = list(int(i) for i in input().split())
    print(calc(a, b, P))


def calc(f, t, P):
    if f in P:
        return "NO"
    elif t in P:
        return "NO"
    elif len(list(set(P))) != len(P):
        return "NO"

    return "YES"


if __name__ == '__main__':
    main()
