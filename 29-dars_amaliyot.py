#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:21:49 2023

@author: user-pc

AMALIYOT
 Asosiy masalaning qo'yilishi:
    1. Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
    2. Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
       * get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    3. Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
       * update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
    4. Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
    5. Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
    6. Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
    7. Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
    dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

"""
# dastur kodi
class Avto:
    """Avtomobil klassi"""
    def __init__(self,model,rang,korobka,narh):
        """Avto klassining xususiyatlari"""
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 0
        
    def get_info(self):
        """Avto haqida m'lumot chiqaradi"""
        info1 = f"Avtomobil: {self.model}, rangi: {self.rang},"
        info1 += f" korobka: {self.korobka}, narxi: {self.narh}$, {self.kilometr} km yurgan."
        return info1
    
    def update_km(self):
        """Avto yuradigan kmni 10 kmga oshirish"""
        self.kilometr +=10
        
class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self,salon_nomi,manzili):
        """Avtosalon klasi xususiyatlari"""
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuv_avtolar = []
        self.sotuv_avtolar_soni = 0
        
        
    def add_avto(self,avto):
        """Avtosalonga avtolarni qo'shish"""
        self.sotuv_avtolar.append(avto)
        self.sotuv_avtolar_soni +=1
        
    def get_avtosalon(self):
        return [avto.get_info() for avto in self.sotuv_avtolar]
        
avto1 = Avto('malibu','qora','avtomat',20000)
avto2 = Avto('nexia 3','oq','avtomat',10000)
avto3 = Avto('lacetti','qizil','avtomat',15000)

#print(avto1.model)
#print(avto1.get_info())

#avto1.update_km() # avto yurganini 10 km ga oshirish
#print(avto1.get_info())

#Avtosalon ob'ekti
avtosalon1 = Avtosalon('Auto max','Samarqand 67')
print(f"{avtosalon1.salon_nomi} avtosalonidagi avtomobillar")
#Avtosalonga avtoni qo'shish
avtosalon1.add_avto(avto1)
avtosalon1.add_avto(avto2)
avtosalon1.add_avto(avto3)

print(avtosalon1.get_avtosalon())
