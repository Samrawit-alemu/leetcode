class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        binn = binary[2:]
        res_bin = ''.join('1' if c == '0' else '0' for c in binn)
        # print(res_bin)
        res = int(res_bin, 2)
        return res
        