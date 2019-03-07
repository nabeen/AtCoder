#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc010/tasks/abc010_3

# txa, tyaからtxb, tybに移動
# 時間はT分、毎分V


def main() -> None:
    txa, tya, txb, tyb, T, V = map(int, input().split())
    n = int(input())
    pos = [tuple(map(int, input().split())) for _ in range(n)]
    # print(pos)
    for v in pos:
        T1 = (abs(v[0] - txa) ** 2 + abs(v[1] - tya) ** 2) ** (1/2)
        T2 = (abs(v[0] - txb) ** 2 + abs(v[1] - tyb) ** 2) ** (1/2)
        if T1 + T2 <= T * V:
            print("YES")
            exit()
    print("NO")


if __name__ == '__main__':
    main()
