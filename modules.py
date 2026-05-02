import math_functions as mfs
from function import toliq_ism, yosh_hisobla 
import math as m
# from math import sqrt, pow
# print(math.fabs(-8))
print(m.sqrt(16))
# print(math_functions.addition(5, 3))
# print(math_functions.subtraction(8, 5))
# print(math_functions.find_max(8, -5, 91, 100, 10))
# print(function.toliq_ism("Jumagul", "Umrzoqova"))
print(mfs.addition(5, 12))
print(mfs.find_max(8, -5, -4, 12))
print(toliq_ism("Jumavoy", "O'ktamova"))
print(mfs.PI)

# random module
import random as r
print(r.random()) # 0 va 1 oraliqdagi qiymat qaytaradi
print(r.randint(100, 1000))

ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(11))
print(x)
r.shuffle(x)
print(x)