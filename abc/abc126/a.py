#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main() -> None:
    N, K = map(int, input().split())
    S = input()
    print(S[0:K-1] + S[K-1].lower() + S[K:])


if __name__ == '__main__':
    main()
