#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main() -> None:
    S = input()
    a1 = cou(S, '0', '1')
    a2 = cou(S, '1', '0')
    print(min(a1, a2))


def cou(S, f, s):
    num = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == f:
                num += 1
            else:
                pass
        elif i % 2 != 0:
            if S[i] == s:
                num += 1
            else:
                pass
    return num


if __name__ == '__main__':
    main()
