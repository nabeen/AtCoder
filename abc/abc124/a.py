#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main() -> None:
    A, B = map(int, input().split())
    if A == B:
        print(2 * A)
    else:
        print(max(A, B) * 2 - 1)


if __name__ == '__main__':
    main()
