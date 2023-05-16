class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)  # mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26  # 0 for each character a....z

            for c in s:
                count[ord(c) - ord("a")] += 1  # lower case a - a = 0 etc

            res[tuple(count)].append(s)
        return res.values()
