class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            map[key].append(word)

        return list(map.values())
        