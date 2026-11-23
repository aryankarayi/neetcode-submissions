class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        3, 4, 5, 6, 1, 2

        l = 3
        r = 2
        mid = 5

        l = 6
        r = 2
        mid = 1

        l = 6
        r = 1
        mid = 6
        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = ((r - l) // 2) + l

            if l == mid:
                return min(nums[l], nums[r])

            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[l] and nums[mid] < nums[r]:
                r = mid


