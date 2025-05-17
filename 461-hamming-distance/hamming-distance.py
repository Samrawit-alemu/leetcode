class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_val = x ^ y
        cnt = 0

        while xor_val:
            if xor_val & 1:
                cnt += 1
            xor_val >>= 1
        return cnt