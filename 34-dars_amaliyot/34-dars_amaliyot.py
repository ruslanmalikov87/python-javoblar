#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 06:20:07 2023

@author: user-pc

AMALIYOT

#1.Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
2.Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini konsolga chiqaring: talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
3.Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
4.Ushbu JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.
5.Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash tili haqidagi maqolani JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan ma'lumotni JSON ko'rinishida saqlang (brauzerda Ctrl+S tugmasini bosib). Faylni Pythonda oching va konsolga maqolaning sarlavhasi (title) va qisqa matnini (extract) chiqaring: https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python

"""

import json

data = {"Model":"Malibu", "Rang":"Qora",'Yil':2020,'narh':4000}

#json formatiga o'tkazish
data_json = json.dumps(data)
print(data_json)

talaba1 = {'ism':'Hasan','familiya':'Husanov','tyil':2000}
talaba1_json = json.dumps(talaba1,indent = 4)

print("talaba_json formatini konsolga chiqarish")
print(talaba1_json)

#3 data va talabalar json formatini faylga saqlash
with open('data.json','w') as f:
    json.dump(data,f)
    

with open('talaba1.json','w') as f:
    json.dump(talaba1,f)

#4
with open("talaba.json") as f:
    data = json.load(f)
    
    
print(f"{data['ism']} {data['familiya']} 1-kurs Matematika fakultet talabasi ")


#5
    
with open("wikipedia.json") as f:
    wiki = json.load(f)

print(wiki["query"]["pages"]["13801"]["title"])
print(wiki["query"]["pages"]["13801"]["extract"])