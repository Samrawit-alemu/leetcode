class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n=len(nums)
        v=n//2
        b=[]
        for i in range(v):
            min1=min(nums)
            max1=max(nums)
            ave=(min1+max1)/2
            nums.remove(min1)
            nums.remove(max1)
            b.append(ave)
        return min(b)