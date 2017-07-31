#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""


__author__ = "Burak Ünal"


enBuyuk = 0

for i in range(100,999):
    for j in range(100,999):
        carpim = i*j
        if  str(carpim) == str(carpim)[::-1]:
            if carpim > enBuyuk:
                enBuyuk = carpim
print("En Büyük Palindrom Sayı =", enBuyuk)
