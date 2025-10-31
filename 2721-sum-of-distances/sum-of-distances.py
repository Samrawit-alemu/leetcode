class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        hash_map = defaultdict(list)

        for i, num in enumerate(nums):
            hash_map[num].append(i)


        for indices in hash_map.values():
            n = len(indices)
            prefix_sum = 0
            total = sum(indices)

            for i, index in enumerate(indices):
                # left_sum = prefix_sum
                # left_count = i
                right_sum = total - (prefix_sum + index)
                right_count = n - i - 1

                nums[index] = (index * i - prefix_sum) + (right_sum - index * right_count)
                prefix_sum += index
 
        return nums