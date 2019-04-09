#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# N個の店
# M本のドリンク
# A円のドリンクをB本買える
# 最小でいくらあればいいか


def main() -> None:
    N, M = map(int, input().split())
    l = [tuple(map(int, input().split())) for _ in range(N)]
    l.sort()
    yen = 0
    hon = M
    for v in l:
        if hon - v[1] > 0:
            hon -= v[1]
            yen += v[0] * v[1]
        elif hon - v[1] == 0:
            hon -= v[1]
            yen += v[0] * v[1]
            break
        else:
            yen += v[0] * hon
            break
    print(yen)


if __name__ == '__main__':
    main()
