class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
    
        for start, end in nums:
            for point in range(start, end + 1):  # inclusive
                covered.add(point)
        
        return len(covered)