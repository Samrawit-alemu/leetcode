class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-i for i in piles]
        heapq.heapify(heap)
        n_steps = 0
        for _ in range(k):
            largest = heapq.heappop(heap)
            remaining = largest + math.floor(-largest/2)
            heapq.heappush(heap, remaining)
            n_steps += 1

        return -sum(i for i in heap)