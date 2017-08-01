#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""

__author__ = "Burak Ünal"

# yaklaşık 4 dakika sürüyor hesaplaması // daha iyi bir algoritma kurabilirsem güncellerim.

sayi = 1
durum = True
sayac = 2 # Asal olan 2 yi dahil etmediğimiz için sayacı 2 den başlatıyorum.

print("1. Asal Sayı = 2")
while True:
    sayi+=2
    for i in range(2,int(sayi/2)):
        if sayi%i == 0:
            durum = False
    if durum==True and sayi != 1:
        print(sayac,"."," Asal sayı = ", sayi, sep="")
        sayac+=1
        if sayac == 10002:
            quit()

    durum = True



