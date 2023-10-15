#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:22:58 2023

@author: user-pc

AMALIYOT

Quyidagi funksiyalarni yarating, va ularning har biri uchun test dasturlarini yozing:

    Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
    Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya
    Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya
    Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi funksiya yozing.


"""

#1 uchta sondan kattasini topuvchi funksiya
def uch_son_taq(a,b,c):
    if a>b:
        max = a
    else:
        max = b
        
    if max>c:
        max = max
    else:
        max = c
    return max
        
print(uch_son_taq(3,4,5))

#2 matndan iborat ro'yxat tuzing

def matn_roy(matnlar):
   for i in matnlar:
       print(i.title(),' ',end='')
    

matn = ['men','sen','u']
print(matn_roy(matn))

#3 juft sonlar
def juft_son(sonlar):
    for son in sonlar:
        if son%2 == 0:
            print(son,',',end='')
            
aa=[12,30,44,41,45,36,26]
print(juft_son(aa))

#4 fibbonachi sonlari
def fibbonachi(n):
    if n < 0:
        print("0 dan kichik son kiritdingiz")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibbonachi(n-1) + fibbonachi(n-2)
    
# fibbonachi sonlarni chiqaruvchi operator
for i in range(10):
    print(fibbonachi(i),',',end='')
