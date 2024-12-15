class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
                

solution = Solution()

nums = [2,7,11,15]
target = 9
output = solution.twoSum(nums, target)

print("Input: nums " + str(nums) + ", target " + str(target))
print("Output: " + str(output)) 
