class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,}

        result, idx  = 0, 0

        while (idx < len(s)):
            next_idx = idx + 1
            a = data.get(s[idx])

            if next_idx < len(s):
                b = data.get(s[next_idx])
                if a >= b:
                    result += a 
                    idx += 1 
                else:
                    result += b - a 
                    idx += 2
            else:
                result += a 
                idx += 1

        return result
            
