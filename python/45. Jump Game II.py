class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] >= (len(nums) - 1):
            return 1
        max_idx = 0
        counter = 0
        slice_idx = -1
        for i in range(len(nums)):
            if i + nums[i] > max_idx:
                max_idx = nums[i] + i
            if max_idx >= len(nums) - 1:
                counter += 1
                break
            if i >= slice_idx:
                slice_idx = max_idx
                counter += 1
        return counter
