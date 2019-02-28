#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc022/tasks/abc022_a


def main() -> None:
    N, S, T = map(int, input().split())
    A = list(int(input()) for _ in range(N))
    ans = 1 if S <= A[0] <= T else 0
    w = A[0]
    for i in A[1:]:
        w = w + i
        if S <= w <= T:
            ans = ans + 1
    print(ans)


if __name__ == '__main__':
    main()
