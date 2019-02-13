#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc111/tasks/arc103_a

from collections import Counter


def main() -> None:
    n = int(input())
    p = [int(i) for i in input().split()]

    # 奇数番目の配列
    l1 = [int(p[i]) for i in range(0, n, 2)]
    # 偶数盤面の配列
    l2 = [int(p[i]) for i in range(1, n, 2)]

    if len(set(p)) == 1:
        # ゾロ目判定
        print(n // 2)
    else:
        lc1 = Counter(l1).most_common(2)
        lc2 = Counter(l2).most_common(2)

        if lc1[0][0] == lc2[0][0]:
            # 最頻値がかぶってしまった場合
            print(n - max(lc1[0][1] + lc2[1][1], lc1[1][1] + lc2[0][1]))
        else:
            # かぶっていなかったら最頻値を引く
            print(n - lc1[0][1] - lc2[0][1])


if __name__ == '__main__':
    main()
