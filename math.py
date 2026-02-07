# Python math module
import math
# constants - o'zgarmas qiymatlar
# pi = 3.1415
print(math.pi)
# e = 2.71
print(math.e)
# functions - funksiyalar
# modul
print(math.fabs(-5))
print(math.fabs(7))
# kvadrat ildiz x ** 0.5 = x ** 1/2
square_root = math.sqrt(625)
print(square_root)

print(5 ** 3) # 125
print(math.pow(5, 3))
x, y = 8, 2
print(math.pow(y, x))
# 3! = 1 * 2 * 3 = 6; 5! = 1 * 2 * 3 * 4 * 5
# print(math.factorial(5))
# print(math.factorial(10))
# up rounding - yuqoriga yaxlitlash
# print(math.ceil(5.48)) 
# print(math.ceil(5.12))
# print(math.ceil(5.74)) # 6
# print(math.ceil(5)) # 5
# # down rounding - pastga yaxlitlash
# print(math.floor(5.48)) 
# print(math.floor(5.12))
# print(math.floor(5.74)) # 5
# print(math.floor(5)) # 5

print(math.sin(math.radians(30)))
print(math.sin(math.radians(90)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(45)))
print(1 / math.tan(math.radians(30)))
# tg * ctg = 1 => ctg = 1 / tg 

print(math.exp(3))