class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        ans=1
        for n in nums:
            ans *= n
            
        if ans>0: return 1
        if ans<0: return -1
        if ans==0: return 0
