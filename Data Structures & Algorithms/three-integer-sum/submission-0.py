class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while True:
                if l == r or l > r:
                    break
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    if [nums[i],nums[l],nums[r]] not in pairs:
                        pairs.append(list([nums[i],nums[l],nums[r]]))
                    r -= 1
                    l += 1
        return pairs






        