#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc022/tasks/abc022_b


def main() -> None:
    N = int(input())
    A = list(int(input()) for _ in range(N))
    print(len(A) - len(set(A)))


if __name__ == '__main__':
    main()
