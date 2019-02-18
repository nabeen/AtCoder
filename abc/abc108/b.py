#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc108/tasks/abc108_b


def main() -> None:
    X1, Y1, X2, Y2 = map(int, input().split())
    X3, Y3 = X2-(Y2-Y1), Y2+(X2-X1)
    X4, Y4 = X3-(X2-X1), Y3-(Y2-Y1)
    print(str(X3) + " " + str(Y3) + " " + str(X4) + " " + str(Y4))


if __name__ == '__main__':
    main()
