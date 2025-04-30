class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        oper = 0
        while nums[0] < k and nums:
            if len(nums) < 2:
                return -1

            x = heappop(nums)
            y = heappop(nums)
            val = min(x,y) * 2 + max(x,y)
            heappush(nums, val)
            oper += 1
        return oper
    