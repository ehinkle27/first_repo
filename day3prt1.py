# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:34:31 2018

@author: earl
"""

#number = int(input("Enter a number: "))
number = int(input("Enter a number: "))
factor = number
for num in range(number):
    if num == 0:
        continue
    print(num)
    factor = factor*num    
print(factor)
