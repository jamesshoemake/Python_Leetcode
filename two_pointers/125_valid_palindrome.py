# blind 75 question
# easy example using builtin Python methods
# uses extra memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# pointer solution that does not use extra memory


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    # ord method gives ascii value for a character
    def alphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord("Z")) or
                (ord('a') <= ord(c) <= ord("z")) or
                (ord('0') <= ord(c) <= ord("9")))


# solver = Solution2
# print(solver.isPalindrome(solver, s="A man, a plan, a canal: Panama"))
