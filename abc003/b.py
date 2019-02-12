#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc003/tasks/abc003_2


def main() -> None:
    a = input()
    b = input()
    atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] == "@" and b[i] in atcoder:
            continue
        elif b[i] == "@" and a[i] in atcoder:
            continue
        else:
            print("You will lose")
            exit()

    print("You can win")


if __name__ == '__main__':
    main()
