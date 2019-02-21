#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 


def main() -> None:
    a, b = map(int, input().split())
    h = 0
    for i in range(1, 1000):
        if (h - a) == (h + i - b):
            print("{}".format(h - a))
            break
        else:
            h = h + i


if __name__ == '__main__':
    main()
