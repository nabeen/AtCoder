#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc120/tasks/abc120_d

# TODO: 解説動画を写経しただけなので中身を理解する
# N島
# M橋


class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [-1 for _ in range(n)]

    def root(self, a: int) -> int:
        if self.par[a] < 0:
            return a
        else:
            self.par[a] = self.root(self.par[a])
            return self.par[a]

    def size(self, a: int) -> int:
        return -self.par[self.root(a)]

    def connect(self, a: int, b: int) -> bool:
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return False

        if self.size(a) < self.size(b):
            a, b = b, a

        self.par[a] = self.par[a] + self.par[b]
        self.par[b] = a

        return True


def main() -> None:
    N, M = map(int, input().split())
    t = [tuple(map(int, input().split())) for _ in range(M)]
    ans = [0 for _ in range(M)]
    ans[-1] = N * (N - 1) // 2
    uni = UnionFind(N)
    for i in reversed(range(1, M)):
        ans[i - 1] = ans[i]
        a = t[i][0] - 1
        b = t[i][1] - 1
        if uni.root(a) != uni.root(b):
            ans[i - 1] = ans[i - 1] - uni.size(a) * uni.size(b)
            uni.connect(a, b)

    for v in ans:
        print(v)


if __name__ == '__main__':
    main()
