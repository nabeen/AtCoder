#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc112/tasks/abc112_c

# ht + |px − xt| + |py − yt|(ht ≥ 1)
# 中心座標(CX, CY)、高さHを求める
# 座標(x, y)の高さhは、h = H - abs(x - CX) - abs(y - CY)


def main() -> None:
    N = int(input())
    pos = [[int(i) for i in input().split()] for _ in range(N)]
    pos = sorted(pos, key=lambda x: x[2], reverse=True)
    x, y, h = pos[0]
    for CX in range(101):
        for CY in range(101):
            H = h + abs(x - CX) + abs(y - CY)
            if all(posh == max(H - abs(posx - CX) - abs(posy - CY), 0) for posx, posy, posh in pos):
                print('{x} {y} {h}'.format(x=CX, y=CY, h=H))
                exit()


if __name__ == '__main__':
    main()
