# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:47:19 2018

@author: earl
"""
Userletter = input("enter a letter to analyse: ")
userstring = input("Enter a phrase: ")
lettercount = 0

for letter in userstring:
    if Userletter.upper == letter.upper:
        lettercount += 1
print(lettercount)