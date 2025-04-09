class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # graph = defaultdict(list)
        # visit = set()
        # for i,j in trust:
        #     graph[i].append(j)
        # for i in range(1,n+1):
        #     if len(graph[i]) == 0 and sum(j in i for i in graph.values())== n-1:
        #         return i
        # return -1
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for i,j in trust:
            outdegree[i] += 1
            indegree[j] += 1
        for i in range(1,n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1
                