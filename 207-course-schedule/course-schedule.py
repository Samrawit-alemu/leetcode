class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # white, grey, black = 0,1,2
        # if cyclic not possible else possible
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
      
        colors = [0 for course in range(numCourses)]
        def dfs(course):
            if colors[course] == 1:
                return False
            elif colors[course] == 2:
                return True
            colors[course] = 1
            for child in graph[course]:
                if not dfs(child):
                    return False
            colors[course] = 2
            return True
        for course in range(numCourses):
            if colors[course] == 0:  # Not visited yet
                if not dfs(course):
                    return False
        
        return True
   

