#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc109/tasks/abc109_b


def main() -> None:
    N = int(input())
    say = [input() for _ in range(N)]
    if len(say) != len(list(set(say))):
        print("No")
        exit()
    else:
        for i in range(N-1):
            if say[i][-1] != say[i+1][0]:
                print("No")
                exit()
            else:
                continue
    print("Yes")


if __name__ == '__main__':
    main()
