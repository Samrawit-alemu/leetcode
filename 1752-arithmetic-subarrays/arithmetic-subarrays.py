class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []

        for i in range(len(l)):
            sub_arr = nums[l[i]:r[i]+1]
            sub_arr.sort()
            dif = sub_arr[1] - sub_arr[0]
            flag = True

            for j in range(1,len(sub_arr)):
                if sub_arr[j] - sub_arr[j-1] != dif:
                    flag = False
                    break
            ans.append(flag)
        return ans
        