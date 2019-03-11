#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc024/tasks/abc024_a


def main() -> None:
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())
    if S + T >= K:
        print((A - C) * S + (B - C) * T)
    else:
        print(A * S + B * T)


if __name__ == '__main__':
    main()
