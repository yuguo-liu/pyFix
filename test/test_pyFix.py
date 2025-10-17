'''
Author: Yuguo Liu
Date: 2025-10-17 16:52:14
LastEditors: Yuguo Liu
LastEditTime: 2025-10-17 17:07:58
Description: 
FilePath: /pyFix/test/test_pyFix.py
'''
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from pyFix import pyFix

if __name__ == '__main__':
    a = pyFix(1.0, 8, 8)
    print(a)
    print(repr(a))