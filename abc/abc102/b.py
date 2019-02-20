#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc102/tasks/abc102_b


def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    AS = sorted(A)
    print(abs(AS[0] - AS[-1]))


if __name__ == '__main__':
    main()
