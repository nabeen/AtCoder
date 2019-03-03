#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc120/tasks/abc120_b


def main() -> None:
    A, B, K = map(int, input().split())
    ans = []
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            ans.append(i)

    ans.sort(reverse=True)
    print(ans[K - 1])


if __name__ == '__main__':
    main()
