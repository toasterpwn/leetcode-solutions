class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(nums)):
            for x in range(len(nums)):
                if nums[i] + nums[x] == target:
                    if i in final or x in final:
                        break
                    else:
                        final.append(i)
                        final.append(x)
            
        return final
                    