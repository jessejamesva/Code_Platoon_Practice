"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        checked = {}

        for i in s:
            if i in checked:
                checked[i] += 1
            else:
                checked[i] = 1
        
        for i in t:
            if i not in checked:
                return False

            else: 
                if checked[i] == 0:
                    return False
                checked[i] -= 1

        return len(checked) != 0