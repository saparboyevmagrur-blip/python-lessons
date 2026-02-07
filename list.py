# List - ro'yxat, massiv
# fruit = 'apple'
# fruit2 = 'grape'
# fruit3 = 'banana'
# print(fruit2)
# fruit2 = 'cherry'
# print(fruit2)
# fruits = ['apelsin', 'grape', 'banana', 'apple']
# print(fruits)
# List elementi index orqali olinadi
# Dasturlashda indekslash 0 dan boshlanadi
# List elementini olish 
# print(fruits[1], fruits[3])
# mix_data = [12, -5, 5.75, 'test', True, 'dev', 15, 78, 99, 1000, False, 'front', [1, -5]]
# print(type(fruits)) # list
# list elementini o'zgartirish
# fruits[1] = 'cherry'
# print(fruits)
# list uzunligi(length) - ro'yxatda saqlangan elementlar soni
# print(len(fruits))
# print(len(mix_data))
# listdagi so'nggi elementni topish
# first element
# print(mix_data[0])
# last element
# length = len(mix_data)
# last_index = length - 1
# last_element = mix_data[last_index]
# print(last_element)

# Ro'yxat elementlari ustida amallar
numbers = [12, -15, 88.99, 10, 15.93, -8.75]
# 1. Ro'yxat elementini o'zgartirish
numbers[1] = 20
# print(numbers)

# Ro'yxatga yangi element qo'shish
# 1. list.append(new_element) method
numbers.append(17)
numbers.append(-102.89)
# print(numbers)

# 2. list.insert(index, element) method
numbers.insert(2, 13)
# print(numbers)
numbers.insert(0, 0)
# print(numbers)

# CRUD - create / read / update / delete
# Ro'yxat elementini o'chirish
# 1. list.remove(element) method
numbers.remove(0)
# print(numbers)
numbers.remove(numbers[3])
# print(numbers)

# 2. del operator
del numbers[5]
# print(numbers)

# Ro'yxatdagi elementni sug'urib olish
# list.pop(index?) method
number = numbers.pop(2)
# print(number)
# print(numbers)
# last_element = numbers.pop()
# print(last_element)

ismlar = ['Abror', 'Bobur', 'Diyor', 'Bekzod']
print(f"Salom {ismlar[0]}, bugun choyxona bormi? \n{ismlar[2]} choyxonaga boramizmi?")

sonlar = [12, -5, 77, 15.89, 18.72, 0.25]
print(sonlar[2] + sonlar[1]) # 77 + (-5)
print(sonlar[0] / sonlar[5]) # 12 / 0.25
# 15.89 => -15.25
sonlar[3] = -15.25
print(sonlar)
sonlar[2] = 100
print(sonlar)
t_shaxslar = ['Al-Xorazmiy', 'Imom Buxoriy', 'Amir Temur', "Alisher Navoiy"]
z_shaxslar = ['Ilon Musk', 'Bill Gates', 'Steve Jobs', 'Pavel Durov']
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\nzamonaviy shaxslardan esa {z_shaxslar.pop(2)} bilan\nsuhbat qilishni istar edim")