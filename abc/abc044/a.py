#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc044/tasks/abc044_a


def main() -> None:
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())
    if N >= K:
        print(K * X + (N - K) * Y)
    else:
        print(N * X)


if __name__ == '__main__':
    main()
