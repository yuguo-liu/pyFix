'''
Author: Yuguo Liu
Date: 2025-10-11 11:48:35
LastEditors: Yuguo Liu
LastEditTime: 2025-10-11 11:48:58
Description: 
FilePath: /pyFix/exp/hadamardProd.py
'''
import time
import numpy as np

vector_length = 10**6

vector1 = np.random.rand(vector_length)
vector2 = np.random.rand(vector_length)


def hadamard_product_basic(v1, v2):
    return [v1[i] * v2[i] for i in range(len(v1))]


def hadamard_product_np(v1, v2):
    return np.multiply(v1, v2)


start_time = time.time()
hadamard_product_basic(vector1, vector2)
basic_duration = time.time() - start_time


start_time = time.time()
hadamard_product_np(vector1, vector2)
np_duration = time.time() - start_time


print(f"Basic Python Implementation Time: {basic_duration:.6f} seconds")
print(f"NumPy Implementation Time: {np_duration:.6f} seconds")


speedup = basic_duration / np_duration
print(f"Speedup of NumPy over basic Python: {speedup:.2f}x")
