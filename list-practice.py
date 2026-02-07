# List bilan ishlash
# list methods
# 1. list.append(element)
# 2. list.insert(index, element)
# 3. list.remove(element)
# 4. list.pop(index?)
# 5. list.sort()
cars = ['bmw','mercedes benz', 'volvo', 'damas', 'general motors', 'tesla', 'audi']
# cars.sort() # alifbo(english) ketma-ketlik bo'yicha tartiblash
# print(cars)
# cars.sort(reverse=True) # reverse(teskari)
# print(cars)
sorted_list = sorted(cars)
reversed_sort_list = sorted(cars, reverse=True)
print(cars)
print(sorted_list)
print(reversed_sort_list)

ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort() # o'sish tartibi
print(ages)
print(sorted(ages, reverse=True)) # kamayish tartibi

# list.reverse() 
fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)
print(len(fruits)) # 5

# list() funksiyasi
users = ['akmal', 'farzona', 'shodlik']
students = list(('jamol', 'asal', 'kamol', 'zebo')) # ['jamol', 'asal', 'kamol', 'zebo']
print(students)
# range() funksiyasi - ma'lum bir oraliqdagi sonlarni shakllantirish uchun ishlatilanadi
# range(start, stop, step?)
# step = 1(default value)
# range(0, 10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(2, 20, 2) # 2, 4, 6, 8, ... 16, 18
sonlar = list(range(0, 10))
juft_sonlar = list(range(2, 21, 2))
print(sonlar)
print(juft_sonlar)

# min() - eng kichik, max() - eng katta, sum() - yig'indi
# min(12, 15, 56, -2, 0, 99) # -2
narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874] 
eng_arzoni = min(narxlar)
eng_qimmati = max(narxlar)
print(eng_arzoni)
print(eng_qimmati)
yigindi = sum(narxlar)
print(yigindi)

# listni kesish
techs = ['AI', 'Robot', 'Python', 'DB', 'Chat GPT', 'Web']
# new_list = list[start : end]
my_techs = techs[2 : 5]
print(my_techs)
print(techs[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(techs[2:]) # 2-indexdagi elementdan boshlab ro'yxat oxirigacha kesib oladi