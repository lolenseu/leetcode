class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        balance = 0

        for char in s:
            if char == '(':
                if balance > 0:  
                    result.append(char)
                balance += 1
            elif char == ')':
                balance -= 1
                if balance > 0: 
                    result.append(char)

        return ''.join(result)


solution = Solution()

input_string = "(()())(())"
output_string= solution.removeOuterParentheses(input_string)

print("Input:" + input_string )
print("Output:" + output_string)