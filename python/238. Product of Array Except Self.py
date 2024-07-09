class Solution:
    def prefixProduct(self, idx: int) -> List[int]:
        if idx < 0:
            return 1
        elif self.prefix[idx] == 31:
            self.prefix[idx] = self.prefixProduct(idx-1)*self.nums[idx]
        return self.prefix[idx]
    
    def suffixProduct(self, idx: int) -> List[int]:
        if idx >= len(self.suffix):
            return 1
        
        elif self.suffix[idx] == 31:
            self.suffix[idx] = self.suffixProduct(idx+1)*self.nums[idx]

        return self.suffix[idx]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.prefix = [31]*len(nums)
        self.suffix = [31]*len(nums)
        result = [0]*len(nums)

        for i in range(len(nums)):
            result[i]= self.prefixProduct(i-1)*self.suffixProduct(i+1)
        return result