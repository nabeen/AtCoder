#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc098/tasks/abc098_b


def main() -> None:
    N = int(input())
    S = input()
    m = 0
    for i in range(N):
        same_num = len(set(sorted(S[0:i])) & set(sorted(S[i:])))
        m = same_num if m < same_num else m
    
    print(m)


if __name__ == '__main__':
    main()
