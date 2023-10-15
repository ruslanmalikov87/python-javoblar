#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:42:14 2023

@author: user-pc

AMALIYOT

1. Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
2. Quyidagi pi_million_digits.txt faylini yuklab oling (faylda 𝜋 soni nuqtadan so'ng million xona aniqlik bilan yozilgan).
3. Sizning tug'ilgan kuningiz 𝜋 soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
4. Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
5. Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing. Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas).

"""
import pickle

with open('pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = pi.replace(' ','')

print(pi)
# Tug'ilgan kunim pi da bormi?
bdate = '31122000'
print(bdate in pi)


pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz

with open('pi_float.dat','wb') as file:
    pickle.dump(pi,file)