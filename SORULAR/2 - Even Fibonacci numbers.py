#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
__author__ = "Burak Ünal"


sayi1 = 1
sayi2 = 2
hedef= 0
cift_toplam = 0

while (hedef <= 4000000):
    hedef = sayi1+sayi2
    sayi1 = sayi2
    sayi2 = hedef
    if hedef%2==0:
        cift_toplam += hedef

print("Sonuç =",cift_toplam+2)
