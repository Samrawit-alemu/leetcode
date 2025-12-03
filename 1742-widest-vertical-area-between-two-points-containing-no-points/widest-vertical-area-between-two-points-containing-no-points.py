class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_axis = []
        diff = []
        n = len(points)
        for i in range(n):
            x_axis.append(points[i][0])
        x_axis.sort()
        # print(x_axis)
        for j in range(1,n):
            diff.append(x_axis[j] - x_axis[j-1])
        print(diff)
        return max(diff)
