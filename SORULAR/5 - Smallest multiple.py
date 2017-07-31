#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


__author__ = "Burak Ünal"


sayi = 20
b_toplami = 0 # bölenlerin toplamı 210 olmalıdır.
while True:
    for i in range(1,21):
        if sayi%i==0:
            b_toplami+=i
            if b_toplami==210:
                print("Sonuç =",sayi)
                quit()
        else:
            b_toplami=0
            sayi+=10
            break