#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main() -> None:
    A, B, T = map(int, input().split())
    if T // A < 0:
        print(0)
    else:
        print((T // A) * B)


if __name__ == '__main__':
    main()
