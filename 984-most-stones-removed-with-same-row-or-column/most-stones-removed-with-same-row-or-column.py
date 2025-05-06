class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0 for i in range(n)]
    def find(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.find(self.parent[x])
    def union(self,x,y):
        r_x=self.find(x)
        r_y=self.find(y)
        if r_x!=r_y:
            if self.rank[r_x] > self.rank[r_y]:
                self.parent[r_y] = r_x
            elif self.rank[r_x] < self.rank[r_y]:
                self.parent[r_x] = r_y
            else:
                self.parent[r_x] = r_y
                self.rank[r_y] += 1 

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf=UnionFind(n)
        for x in range(n):
            for y in range(n):
                if stones[x][0] == stones[y][0] or stones[x][1] == stones[y][1]:
                    uf.union(x,y)
        s=set()
        for i in range(n):
            s.add(uf.find(i))
        return n-len(s)

        