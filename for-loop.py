# Loop - sikl
# 1. for loop # 2. while loop
# students = ["Charos", "Kumush", "Akmal", "Ozodbek", "Xudoyshukur", "Asal"]
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])
# for student in students:
#     print(f"Hurmatli {student}, sizni interviewga taklif qilamiz")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi")

nums = list(range(1, 11))
for number in nums:
    # print(number)
    print(f"{number} sonining kvadrati {number ** 2} ga teng")

sonlar = list(range(20))
# start_default_value = 0
print(sonlar) # [0, 1, ... 18, 19]
# [0, 1, 4, 9, 16, ..., 324, 361]
sonlar2 = []
for son in sonlar:
    sonlar2.append(son ** 2)

print(sonlar2)

# 2-usul
for index in range(len(sonlar)):
    print(index) # element indexi
    print(sonlar[index]) # element

# 1-marta => index = 0 => sonlar[0] = 0
# 2-marta => index = 1 => sonlar[1] = 1
# 3-marta => index = 2 => sonlar[2] = 2
# ...
# 20-marta => index = 19 => sonlar[19] = 19

# Amaliyot:
# 1. 1 dan 101 gacha bo'lgan sonlarni chiqaring
# sonlar3 = list(range(1, 101))
# for element in sonlar3:
#     print(element)

# for number in range(1, 101):
#     print(number)

# 2.
# names=['Kumush','Farida','Gulchehra','Charos','Kumushoy']
# for name in names:
#     print(name)
# print(f"Kod {len(names)} marta takrorlanadi")

# toq_sonlar = list(range(11,100,2))
# for number in toq_sonlar:
#     print(number ** 3)


# kinolar = []

# for n in range(5):
#     kino = input(f"{n+1}-kinoni kiriting: ")
#     kinolar.append(kino)
# print(kinolar) 

# inson_soni= int(input("nechta odam bilan uchrashdingiz? "))
# insonlar=[]
# for n in range(inson_soni):
#     inson=input(f"{n+1} - insonni ismini kiriting ")
#     insonlar.append(inson)

# print(insonlar)


# Nechta do'stingiz bor?
# 1-do'stingiz ismi: Alibek
# 2-do'stingiz ismi: Valijon

# 4 ta o'zingiz yoqtirgan telefonni kiritish topshiriq
# 1-siz yoqtirgan telefon nomini kiriting: 
# 2-siz
# 3-siz
# 4-siz
# Siz yoqtirgan telefonlar ro'yxati: ["iPhone 17 Pro Max orange", "S 25 Ultra"]

# dostlar_soni = int(input("Nechta dostingiz bor? "))
# dostlar =[]
# for n in range(dostlar_soni):
#   dost = input(f"{n+1} dostingizni kiriting: ")
#   dostlar.append(dost)
  
# print(dostlar)

# telefonlar_soni = int(input("sizga nechta telefon modeli yoqadi: "))
# telefonlar = []
# for n in range(telefonlar_soni):
#     telefon = input(f"{n + 1} telefon modelini kiriting: ")
#     telefonlar.append(telefon)
# print(telefonlar)

# numbers = [69, 18, 89, 12, 75, 82, 5, 26]
# min_value = min(numbers)
# results = []
# for number in numbers:
#     results.append(number / min_value)

# print(results)
# [13.8, 3.6 ]

# print(sum(numbers))
# s = 0
# for number in numbers:
#     s += number # s = s + number
# print(s)

# 1 dan 50 gacha juft sonlar yig'indisi

# s = 0
# for son in range(2 , 50 , 2):
#     s += son
# print(s)

# n! = 1 * 2 * 3 * ... (n - 1) * n
# kopaytma = 1
# for son in range(1, 11):
#     kopaytma *= son # kopaytma = kopaytma * son 
# print(kopaytma)

# 1 dan 20 gacha toq sonlar ko'paytmasini yigindisiga nisbatini toping

# kopaytma = 1
# s = 0
# for son in range(1, 20 , 2):
#     kopaytma *= son
#     s += son
    
# print(kopaytma / s)

# nums = [24, 50, 72, 96, 95]
# s = 0
# for son in nums:
#     s += son ** 2
# print(s)

# o'rtacha qiymat = s / length
# s = 0
# for son in nums:
#     s += son
# length = len(nums)
# k = s / length
# print(k)

# nums = [12, -5, 15, 89, -75, -18]
# musbat elementlar yig'indisi
# manfiy elementlar ko'paytmasi
# s = 0
# k = 1
# for son in nums:
#     # print(son)
#     if son > 0:
#         s += son
#     else:
#         k *= son

# print(s)
# print(k)

# 1 dan 20 gacha bo'lgan sonlardan juftlarini ko'paytmasini toqlarini yig'indisiga nisbati
# kopaytma = 1
# s = 0
# for n in range(1, 20):
#     if n % 2 == 0:
#         kopaytma *= n
#     else:
#         s += n
# print(kopaytma / s)

# nums = [12, -5, 15, 89, -75, 18]
# o'rta_arifmetik = s / length
# o'rta_geometrik = ko'paytma
# s = 0
# for number in nums:
#     s += number

# length = len(nums)
# average_value = s / length
# print(average_value)

# import math
# k = 1
# for son in nums:
#     k *= son

# ortacha = math.pow(k, 1 / len(nums))
# print(ortacha)

# numbers = [7, 97, -58, 90]
# Plan
# 1. Juft qiymatlar yig'indisi
# 2. Juft qiymatlar soni
# 3. Juftlarini o'rtachasi
# s = 0
# counter = 0
# for son in numbers:
#     if son % 2 == 0:
#         s += son # s = s + son
#         counter += 1

# print(s / counter)
# k = 0
# nums = [97, 97, -92, 14, 22]
# for number in nums:
#     if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#        k += number
# print(k) 

# M = int(input("M sonni kiriting: "))
# sonlar = [12, 88, 30, 87]
# s = 0
# for n in sonlar:
#     if n > M:
#         s += n
# print(s)
# import math
# nums = [44, 34, 42, 83, 43, 64]
# k = 1
# for n in nums:
#     if n % 2 == 0 or n % 5 == 0:
#         k *= n
# print(math.sin(k))

# nums = [76, 12, 51, 50, 98, 17]
# counter = 0
# # plan 1. toq qiymatlar 2. toq qiymatlar yig'indisi 3. toq qiymatlar soni
# s = 0
# for num in nums:
#     if num % 2 == 1:
#         s += num
#         counter += 1

# print(s / counter)

# 115
# m = int(input("M sonni kiriting: "))
# nums = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# s = 0
# for n in nums:
#     if m > n:
#         s += n ** 2

# print(s)

# number = [44, 59, -75, 73]
# k = 0
# s = 0
# for num in number:
#     k += num ** 2
#     s += num

# length = len(number)
# c = s / length
# print(k)
# print(c)
import math
numbers = [7, 24, -5, 23, 99, -3, 24, 51]
# plan 1. o'rtacha qiymati # 2. manfiy elementlari
# 3. manfiy elementlarini o'_q log almashtirsh
s = 0
for number in numbers:
    s += number
average_value = s / len(numbers)
log_value = math.log(average_value)
print(log_value) # 3.31

for index in range(len(numbers)):
    if numbers[index] < 0:
        numbers[index] = log_value

print(numbers)