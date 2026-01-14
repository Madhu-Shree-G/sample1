from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            value = nums[i]
            difference = target - value
            if difference in d:
                return [d[difference], i]
            d[value] = i
        return []  # No solution found

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))
