#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc025/tasks/abc025_a


def main() -> None:
    S = input()
    N = int(input())
    sl = []
    for i in range(len(S)):
        for j in range(len(S)):
            sl.append(S[i] + S[j])
    sl.sort()
    print(sl[N - 1])


if __name__ == '__main__':
    main()
