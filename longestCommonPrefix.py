# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:41:11 2021

@author: rvalusa
"""

inputStr = []

def longestCommonPrefix(strs):
    result = ''
    if strs:        
        for cIndex, charStr in enumerate(strs[0]):
            j = 0
            for item in strs[1:]:
                try:
                    if item[cIndex] == charStr:
                        # j = 0
                        continue
                    else:
                        j = 1
                        break
                except Exception as e:
                    print("Oops!", e.__class__, "occurred.")
                    j = 1
                    break
                    
            if j == 1:
                break
            
            result +=  charStr    

    return result
        
result = longestCommonPrefix(inputStr)
        
        

    
            
