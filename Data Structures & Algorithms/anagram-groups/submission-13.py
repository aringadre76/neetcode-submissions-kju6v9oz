class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for s in strs:
            counted = [0] * 26

            for char in s:
                counted[ord(char) - ord('a')] += 1

            count[tuple(counted)].append(s)

        print(count)
        return list(count.values())