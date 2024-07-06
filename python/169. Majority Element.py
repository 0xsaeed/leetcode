class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        for i in dic.keys():
            if dic[i] > len(nums) // 2:
                return i
        return -1