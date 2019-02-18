#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://abc006.contest.atcoder.jp/tasks/abc006_3


def main() -> None:
    N, M = map(int, input().split())
    adult, senior, baby = 2, 3, 4

    if N * baby < M:
        # 一番足の多い子供を集めても足の本数が及ばない
        pass
    if N * adult > M:
        # 一番足の少ない大人を集めての足の本数が超える
        pass
    else:
        for sn in range(2):
            # 老人がいるかいないかの二択
            for an in range(0, N - sn + 1):
                # この時点で子供の人数も確定
                bn = N - sn - an
                if senior * sn + adult * an + baby * bn == M:
                    print(str(an) + " " + str(sn) + " " + str(N-sn-an))
                    exit()
                else:
                    continue

    # 最終的にたどり着かなかったら            
    print("-1 -1 -1")


if __name__ == '__main__':
    main()
