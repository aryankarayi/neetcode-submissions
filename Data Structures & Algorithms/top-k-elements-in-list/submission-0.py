class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        top_k = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:k]

        return [key for key, _ in top_k]
        