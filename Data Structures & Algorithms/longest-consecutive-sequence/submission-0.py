class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)

        longest = 0
        for num in hash:
            if num - 1 not in hash:
                count = 1
                curr = num
                while curr +1 in hash:
                    curr += 1
                    count +=1
                if count > longest:
                    longest = count
        return longest



            

