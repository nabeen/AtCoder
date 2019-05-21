#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main() -> None:
    S = input()
    a = S[:2]
    b = S[2:]
    if ('00' < a < '13') and ('00' < b < '13'):
        print("AMBIGUOUS")
    elif '00' < a < '13':
        print("MMYY")
    elif '00' < b < '13':
        print("YYMM")
    else:
        print("NA")


if __name__ == '__main__':
    main()
