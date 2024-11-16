class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out = ''
        fl = True
        
        strs.sort(key=lambda x: len(x))

        for idx, letter in enumerate(strs[0]):
            for word in strs[1:]:
                if letter != word[idx]:
                    fl = False 
            if fl:
                out += letter
            else:
                break
        return out