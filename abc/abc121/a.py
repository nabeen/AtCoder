#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main() -> None:
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H - h) * (W - w))


if __name__ == '__main__':
    main()
