#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc004/tasks/abc004_3


def main() -> None:
    # 入れ替えるカードの配列
    card = ["1","2","3","4","5","6"]
    # 30回やれば初期状態に戻るので余剰をとる
    N = int(input()) % 30
    for i in range(N):
        i = i % 5
        card[i], card[i+1] = card[i+1], card[i]
    print(''.join(card))


if __name__ == '__main__':
    main()
