class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        num1 = nums[:n]
        num2 = nums[n:]

        for i,j in zip(num1, num2):
            ans.extend([i,j])

        return ans

