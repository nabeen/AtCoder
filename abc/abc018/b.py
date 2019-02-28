#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc018/tasks/abc018_2


def main() -> None:
    S = input()
    Sl = [s for s in S]
    N = int(input())
    l = [tuple(map(int, input().split())) for _ in range(N)]
    for t in l:
        x = t[0] - 1
        y = t[1] - 1
        tmp = Sl[x:y+1]
        tmp.reverse()
        Sl = Sl[:x] + tmp + Sl[y+1:]

    print("".join(Sl))


if __name__ == '__main__':
    main()
