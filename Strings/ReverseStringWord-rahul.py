class Solution:
    def reverseWords(self, s: str) -> str:
        arr=reversed(s.split())
        new_str=" ".join(arr)
        return new_str
str="the sky is blue"
s=Solution()
print(s.reverseWords(str)) # Output: "blue is sky the"