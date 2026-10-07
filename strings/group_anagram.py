class Solution:
    def groupAnagram(self, strs):

        anagrams = {}

        for word in strs:

            key = "".join(sorted(word))

            if key in anagrams:
                anagrams[key].append(word)

            else:
                anagrams[key] = [word]

        return list(anagrams.values())

sol = Solution()

print(sol.groupAnagram(["eat","tea","tan","ate","nat","bat"]))