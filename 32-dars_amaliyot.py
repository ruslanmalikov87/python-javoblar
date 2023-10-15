#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:56:21 2023

@author:Ruslan Malikov

AMALIYOT

1.Avvalgi darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
   *Obyekt haqida ma'lumot (__rerp__)
   *Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eg__ va hokazo)
2.Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), __getitem__,__setitem__, __len__ kabi metodlarni qo'shing.
3.Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
4.Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
5.Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling.


"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    
class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def __getitem__(self):
        pass
    
    def __setitem__(self):
        pass
    
    def __len__(self):
        pass
    
    def __add__(self):
        pass
    
    def __sub__(self):
        pass
    
    def __call__(self):
        pass
        
    def get_fan_info(self):
        return f"{self.nomi}"
        
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = [] 
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        
    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return f"Siz bu fanga yozilmagansiz"
    def get_fanlar_ruyx(self):
        return [fan0.get_info() for fan0 in self.fanlar]

    def __repr__(self):
        return f"{self.ism} {self.familiya} passport: {self.passport} va {self.tyil}-yilda tug'ilgan"
    
    def __eq__(self,y):
        return self.bosqich == y.bosqich
    
    def __lt__(self,y):
        return self.bosqich < y.bosqich



fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Informatika")

talaba1 = Talaba("Ruslan","Malikov","AA1234567",1987,"0000123")
talaba2 = Talaba("Rustam","Mardiyev","AB1234567",1990,"0000125")

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)

print(talaba1)
print(talaba2)

#solishtirish
print(f"talabalarni bosqichlari tengmi?")
print(talaba1 == talaba2)
print(talaba1<talaba2)


#aa=talaba1.nomi.get_fan_info()
#print(aa)

