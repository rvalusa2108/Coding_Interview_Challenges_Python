# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:09:12 2021

@author: rvalusa
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != abs(x):
            return False
        
        digitList = []
        while x:
            digit = x % 10
            digitList.append(digit)
            x //= 10 # // is floor division, / is division
        
        reversedDigitList = digitList[::-1]
        
        if digitList == reversedDigitList:
            return True
        else:
            return False



x = 110011
solObject = Solution()
result = solObject.isPalindrome(x)
