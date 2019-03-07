#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc023/tasks/abc023_c


def main() -> None:
    R, C, K = map(int, input().split())
    N = int(input())
    rc = list(tuple(map(int, input().split())) for _ in range(N))
    print(rc)


if __name__ == '__main__':
    main()
