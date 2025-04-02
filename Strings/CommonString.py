class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs:
            if word == "":
                return ""
        if len(strs) == 1:
            return strs[0]
        common_prefix = ""
        j = 0
        Common = True
        while Common:
            for i in range(len(strs) - 1):
                try:
                    if strs[i][j] != strs[i + 1][j]:
                        Common = False
                        break
                except IndexError:
                    Common = False
                    break
            else:
                common_prefix += strs[0][j]
                j += 1
        return common_prefix
strs = ["flower", "flow", "flight"]
s = Solution()
print(s.longestCommonPrefix(strs))  # Output: "fl"
# Explanation: The longest common prefix is "fl".