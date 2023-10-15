#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:49:18 2023

@author: user-pc
"""

import unittest
from dars36_amaliyot import uch_son_taq, matn_roy, juft_son, fibbonachi

class SonMatnTest(unittest.TestCase):
    def test_uchsontaq(self):
        self.assertAlmostEqual(uch_son_taq(3,4,5), 5)
        
    def test_matnroy(self):
        self.assertAlmostEqual(matn_roy('men','sen'), 'Men Sen')
        
    def test_juftson(self):
        son11 = [12,10,13,15,18,20]
        self.assertAlmostEqual(juft_son(son11),12)
        
    def test_fibbonachi(self):
        self.assertAlmostEqual(fibbonachi(3),1)
        
unittest.main()