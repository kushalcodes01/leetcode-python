# LeetCode 125 - Valid Palindrome
# Difficulty: Easy
# Approach:
# 1. Keep only letters and numbers
# 2. Convert to lowercase
# 3. Compare with reversed string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        return cleaned == cleaned[::-1]


# Local Testing
if __name__ == "__main__":
    sol = Solution()

    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False