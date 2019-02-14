#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc001/tasks/abc001_3

# Deg Dis
# < 3,600
# < 12,000


def main() -> None:
    deg, dis = map(int, input().split())
    # 風向
    ws = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
    w = deg / 10
    print(w)
    # 風速(秒速変換)
    wps = round((dis / 60), 1)
    print(wps)


if __name__ == '__main__':
    main()
