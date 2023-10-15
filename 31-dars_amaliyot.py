#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 05:33:33 2023

@author: user-pc

AMALIYOT

1.Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
2.Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
3.Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing

"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    def get_passport(self):
        return self.__passport


class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.bosqich = 1
        Talaba.__talabalar_soni +=1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.__idraqam}"
        return info
    @classmethod
    def get_num_talaba(cls):
        return cls.__talabalar_soni
    
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
print(talaba.get_num_talaba())
print(talaba.get_id())
print(talaba.get_info())