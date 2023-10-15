#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:21:46 2023

@author: user-pc

30-dars amaliyot

AMALIYOT

    1. Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
    2. Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
    3. Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
    4. Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
    5. Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
    6. Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
    7. Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
    8. Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
    9. Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.

Amaliyot javobi quyidagi kodda
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



fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Informatika")

talaba1 = Talaba("Ruslan","Malikov","AA1234567",1987,"0000123")

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)

aa=talaba1.nomi.get_fan_info()
print(aa)
