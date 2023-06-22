def isPalindrome(self, s: str) -> bool:
        s2 = [i.lower() for i in s if i.isalnum()]
        return s2[::-1] == s2