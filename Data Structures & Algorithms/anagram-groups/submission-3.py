class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in new_strs:
                new_strs[sorted_s] = [s]
            else:
                new_strs[sorted_s].append(s)
        return list(new_strs.values())




        