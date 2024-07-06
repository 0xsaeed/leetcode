class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if counter < 2:
                    nums[idx] = nums[i]
                    idx += 1
                counter += 1
            else:
                nums[idx] = nums[i]
                counter = 1
                idx += 1
        return idx
