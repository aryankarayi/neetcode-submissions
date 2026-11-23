from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) + 1

        while l <= r:
            mid = ((r - l)  // 2 )+ l
            total_hours = 0

            for pile in piles:
                total_hours += ceil(pile / mid)
            if total_hours <= h:
                r = mid - 1
            else:
                l = mid + 1
        return max(l, mid)


            



        