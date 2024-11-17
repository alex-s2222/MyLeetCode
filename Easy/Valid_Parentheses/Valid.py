class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', 
                    '}':'{',
                    ']':'['
                    }
        stack  = []

        for element in s:
            if element in brackets.values():
                stack.append(element)
            elif stack and element in brackets.keys() and stack[-1] == brackets[element]:
                stack.pop(-1)
            else:
                return False
            
        return True if stack else False