class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heappush(heap,-num)

        while k>1:
            val = -heappop(heap)
            k-=1
        return -heap[0]