from collections import *

inp1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
inp2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

class DSU:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        if x != self.parent[x]: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    ## assign parent[py] to px instead of parent[y] to px. This can create discrepancy for certain test cases. It is better to change at the parent level than the child level.
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

def graphValidTree(inp, n):
    dsu = DSU(n)

    for x, y in inp:
        if dsu.find(x) == dsu.find(y): return False # found a cycle (Not a tree)
        dsu.union(x, y)
    return True

print(graphValidTree(inp1, 5))
print(graphValidTree(inp2, 5))
