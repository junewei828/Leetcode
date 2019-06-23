class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == [] or len(nums) == 1: 
            return [nums]
        output = []
    
        for i in range(len(nums)):
            ele = nums[i]
        
            new_list = nums[:i] + nums[i+1:]
            for p in Solution.permute(self,new_list):
                output.append([ele] + p)
        
        return output
        