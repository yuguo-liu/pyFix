'''
Author: Yuguo Liu
Date: 2025-10-11 11:49:56
LastEditors: Yuguo Liu
LastEditTime: 2025-10-17 17:12:10
Description: 
FilePath: /pyFix/src/pyFix.py
'''

class pyFix:
    def __init__(self, dec: float, int_bit: int, frac_bit: int):
        """
        :param dec     : the decimal of value
        :param int_bit : the length of integer part
        :param frac_bit: the length of fraction part
        """
        self.int_bit    = int_bit
        self.frac_bit   = frac_bit
        self.value      = int(dec * (2 ** frac_bit))
    

    def __str__(self):
        return str(self.value >> self.frac_bit)

    
    def __repr__(self):
        return f"{self.value} ({self.int_bit} | {self.frac_bit})"


    def __add__(self, other):
        if self.int_bit != other.int_bit or self.frac_bit != other.frac_bit:
            pass
        pass