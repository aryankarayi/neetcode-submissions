class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2:
            return [0] * len(nums)
        if nums.count(0) == 1:
            index = nums.index(0)
            res = [0] * len(nums)
            del nums[index]
            sum = 1
            for num in nums:
                sum *= num
            res[index] = sum
            return res
        else:
            sum = 1
            for num in nums:
                sum *= num
            new_list = []
            for num in nums:
                new_list.append(int(sum/num))
            return new_list
        