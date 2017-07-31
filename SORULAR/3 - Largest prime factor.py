#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

__author__ = "Burak Ünal"


sayi = 600851475143
asalBolen = 2
while sayi != 1:
    if sayi%asalBolen == 0:
        sayi /=asalBolen
    else:
        asalBolen+=1
        continue
print("En büyük asal bölen =",asalBolen)
