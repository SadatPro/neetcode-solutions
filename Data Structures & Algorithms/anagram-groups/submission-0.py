class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:

            count = [0]*26

            for char in s:
                count[ord(char) - ord("a")] += 1
            signature = tuple(count)

            ans[signature].append(s)
        return list(ans.values())