#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc103/tasks/abc103_b


def main() -> None:
    S = input()
    T = input()
    flag = False
    for i in range(len(S)):
        if S == T:
            flag = True
            break
        S = S[-1] + S[:-1]
    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
