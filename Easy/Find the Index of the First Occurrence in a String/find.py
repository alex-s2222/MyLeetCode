class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        start = 0
        while start + len_needle <= len(haystack):
            end = start + len_needle
            if haystack[start: end] == needle:
                return start
            start += 1
        return -1
    