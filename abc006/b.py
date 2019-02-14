#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc006/tasks/abc006_2


def main() -> None:
    n = int(input())
    if n == 1 or n == 2:
    	print(0)
    else:
	    print(trb(n))


def trb(n, a=0, b=0, c=1):
	for _ in range(3,n):
		a, b, c = b, c, (a+b+c) % 10007

	return c


if __name__ == '__main__':
    main()
