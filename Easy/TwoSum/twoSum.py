from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for idx, num in enumerate(nums):
        #     next_idx = idx + 1

        #     if next_idx < len(nums):
        #         for next_num in nums[next_idx:]:
        #             if num + next_num == target:
        #                 return [idx, next_idx]
        #             next_idx += 1
                    
        # return False
        hashMap = defaultdict()
        for idx, num in enumerate(nums):
            try:
                value = hashMap[target-num]
                return [idx, value]
            except:
                hashMap[num] = idx