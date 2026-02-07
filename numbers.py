# Data types - Ma'lumot turlari
# 1. String(matn) => "test", 'adminjon'
# 2. Number(son) => 1. Integer(butun son) 5, 6, 0, -12; 2. Float(O'NLIK SON) -5.85, 7.99
# 3. Boolean(mantiqiy qiymat) => 1. True(haqiqat) 2. False(yolg'on)
# a = 20
# b = -30
# c = a + b
# print(c)

# pi = 3.14159
# radius = 10
# diametr = 2 * radius
# l = 2 * pi * radius
# print("Aylana uzunligi: ", l)

# print(40 / 20)

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b)  # 5.0
# print(a*b) # 6.0
# print(a**b) # 8.0
# print(2*(a+b)) # 10.0

# aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shunday yozdik
# print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

# Konstanta(constant) qiymatlar - o'zgarmas qiymatlar
# PI = 3.14
# G = 9.81

# x = 7
# y = 5
# z = -7
# x, y, z = 7, 5, -7
# print(x - z + y) # 19

# TYPECASTING - Ma'lumot turlarini o'zgartirish
# Type checking - Ma'lumot turini tekshirish
# username = "adminjon"
# age = 23
# x = 2.57
# is_student = True
# type() function
# print(type(username)) # 'str'
# print(type("tester")) # 'str'
# print(type(12)) # 'int'
# print(type(age)) # 'int'
# print(type(17.87)) # 'float'
# print(type(x)) # 'float'
# print(type(False)) # 'bool'
# print(type(is_student)) # 'bool'

# firstname = "Jobir" # 'str'
# age = 36 # 'int'
# # "Jobir 36 yoshda"
# message = firstname + " " + str(age) + " yoshda"
# print(message) 

# age = 36
# print(type(age)) # 'int'
# age = str(age) # 36 => "36"
# print(type(age)) # 'str'

# print(str(36.89)) # "36.89"
# print(int(121.89)) # 121
# print(int(15.0)) # 15
# print(int('18')) # '18' => 18

# print(float(18)) # 18.0
# print(float('12.77')) # '12.77' => 12.77

# input() va son bilan ishlash
# yosh = int(input('Iltimos, yoshingizni kiriting: ')) # 15 => "15"
# t_yil = 2025 - yosh
# print(t_yil)

# Amaliyot
# son = int(input("Istalgan son kiriting: "))
# xabar1 = f"{son} ning kvadrati {son ** 2} ga teng"
# xabar2 = f"{son} ning kubi {son ** 3} ga teng"
# xabar1 = str(son) + " ning kvadrati " + str(son ** 2) + " ga teng"
# xabar2 =  str(son) + " ning kubi " + str(son ** 3) + " ga teng"
# print(xabar1)
# print(xabar2)

# amaliyot 2
# yosh = int(input("Yoshingiz nechada: "))
# yil  = 2025 - yosh
# xabar = f"siz {yil}-yilda tug'ulgansiz"
# print(xabar)

# amaliyot 3
# a = float(input("Birinchi sonni kiriting: "))
# c = float(input("Ikkinchi sonni kiriting: "))
# print(f"{a} + {c} = {a + c}")
# print(f"{a} - {c} = {a - c}")
# print(f"{a} * {c} = {a * c}")
# print(f"{a} / {c} = {a / c}")

# Uchburchakning 1-tomonini kiriting: 12
# Uchburchakning 2-tomonini kiriting: 9
# Uchburchakning 3-tomonini kiriting: 8
# Natija: Uchburchak tomonlari 12, 9, 8 bo'lsa, uning yuzi 150.78 ga teng
# a=int(input("Uchburchakning 1-tomonini kiriting: "))
# b=int(input("Uchburchakning 2-tomonini kiriting: "))
# c=int(input("Uchburchakning 3-tomonini kiriting: "))
# p=(a+b+c)/2
# yuza=(p*(p-a)*(p-b)*(p-c))**(1/2)
# print(f"Uchburchak tomonlari {a},{b},{c} bo'lsa, uning yuzi {yuza}.")

# 1-doiraning radiusi: 3
# 2-doiraning radiusi: 7
# 3-doiraning radiusi: 1
# formulasi: s1 = math.pi * r1 ** 2
# Natija: Radiusi 3 ga teng doiraning yuza 12.85 ga teng
import math
r1 = int(input("Birinchi doiraning radiusini kiriting: "))
r2 = int(input("Ikkinchi doiraning radiusini kiriting: "))
r3 = int(input("Uchinchi doiraning radiusini kiriting: "))
# s = pi * r ** 2
s1 = math.pi*r1**2
s2 = math.pi*r2**2
s3 = math.pi*r3**2
print(f"radiusi {r1} bolgan doiraning yuzasi {s1} ga teng")
print(f"radiusi {r2} bolgan doiraning yuzasi {s2} ga teng")
print(f"radiusi {r3} bolgan doiraning yuzasi {s3} ga teng")