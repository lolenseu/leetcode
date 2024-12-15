class Solution(object):
    def divisorGame(self, n):
        return n % 2 == 0


solution = Solution()

n = 2
print("Input: " + str(n))
print("Output: " + str(solution.divisorGame(n))) 

n = 3
print("Input: " + str(n))
print("Output: " + str(solution.divisorGame(n))) 
