class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([(sr,sc)])
        visited = set()
        visited.add((sr,sc))
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        color2 = image[sr][sc]
        def valid(r,c):
            return 0<=r<len(image) and 0<=c<len(image[0]) and (r,c) not in visited
        while q:
            row, col = q.popleft()
            image[row][col] = color

            for r,c in dir:
                new1 = r+row
                new2 = c+col
                if valid(new1,new2) and image[new1][new2] == color2:
                    q.append((new1,new2))
                    visited.add((new1,new2))
        return image