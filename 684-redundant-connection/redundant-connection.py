class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [0 for i in range(n+1)]

        def find(x):
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[x])
            return find(parent[x])
        
        def union(x,y):
            r_x = find(x)
            r_y = find(y)

            if r_x != r_y:
                
                if rank[r_x] > rank[r_y]:
                    parent[r_y] = r_x
                elif rank[r_x] < rank[r_y]:
                    parent[r_x] = r_y
                else:
                    parent[r_x] = r_y
                    rank[r_y] += 1
                return True
            else:
                return False

        for x,y in edges:
            if not union(x,y):
                return [x,y]
