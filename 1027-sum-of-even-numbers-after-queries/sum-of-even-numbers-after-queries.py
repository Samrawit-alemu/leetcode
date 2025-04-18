class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
      l=[]
      s=sum(i for i in nums if i%2==0)
      for v,i in  queries:
         if nums[i]%2==0:
            s-=nums[i]
         nums[i]+=v
         if nums[i]%2==0:
            s+=nums[i]
         l.append(s)
      return l


         
      return l
          
       

        