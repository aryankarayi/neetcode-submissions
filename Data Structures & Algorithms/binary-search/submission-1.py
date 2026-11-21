class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = ((r - l) // 2) + l
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1




        # [-1,0,2,4,6,8]

        '''
        l = 0
        r = 5
        mid = 2

        l = 3
        r = 5
        mid = 4

        l = 3
        r = 4
        mid = 3

        '''

        