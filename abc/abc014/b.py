#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc014/tasks/abc014_2


def main() -> None:
    n, X = map(int, input().split())
    a = list(map(int, input().split()))
    # 2進数にしてプレフィックスを抜いたものを文字列として保持
    xbin_list = list(int(i) for i in bin(X)[2:])
    xbin_list.reverse()
    ans = 0
    for index, v in enumerate(xbin_list):
        if v == 1:
            ans = ans + a[index]
    
    print(ans)


if __name__ == '__main__':
    main()
