class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = total_odd = 0

        for i, x in enumerate(nums):
            if i % 2 == 0:
                total_even += x
            else:
                total_odd += x

        res = 0
        left_even = left_odd = 0

        for i, x in enumerate(nums):
            if i % 2 == 0:
                total_even -= x
            else:
                total_odd -= x
            if left_even + total_odd == left_odd + total_even:
                res += 1

            if i % 2 == 0:
                left_even += x
            else:
                left_odd += x

        return res