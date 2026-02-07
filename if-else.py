# Tarmoqlanish operatori. if - agar, else - aks holda
# age = int(input("Yoshingiz kiriting: "))
# if age < 18:
#     print("Siz hali yoshsiz, kirishga ruxsat yo'q")
# else: 
#     print("Sizga kirishga ruxsat bor") 

# ball = int(input("Imithondan olgan ballingizni kiriting: "))
# if ball < 56:
#     print("Siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70: 
#     print("3 baho oldingiz")
# elif ball >= 70 and ball < 86:
#     print("4 baho oldingiz")
# elif ball >= 86 and ball <= 100:
#     print("5 baho oldinigz")
# else:
#     print("Siz 0 dan 100 gacha ball kiriting")

# age = int(input("Yoshingiz kiriting: "))
# if age < 16:
#     print("Siz passport olishga yoshsiz")
# else:
#     print("Siz passport olish huquqiga egasiz")

# Amaliyot
# 1-mashq
# son = int(input("Xohlagan sonni kiriting: "))
# if son > 0:
#     print("Musbat son")
# elif son == 0:
#     print("Musbat ham emas, manfiy son ham emas")
# else:
#     print("Manfiy son")

# 2-mashq
# son = int(input("Xohlagan sonni kiriting: "))
# if son % 2 == 0:
#     print("Juft son")
# else:
#     print("Toq son")

# 3-mashq
# son = int(input("Xohlagan sonni kiriting: "))
# if son % 5 == 0:
#     print("son 5 ga bo'linadi")
# else:
#     print("son 5 ga bo'linmaydi")

# 4-mashq
# son=int(input("xoxlagan sonni kiriting: "))
# if son % 2 == 0 and son % 3 == 0:
#     print("son 6 ga bo`linadi")
# else:
#     print("son 6 ga bo`linmaydi")

# 5-mashq
# a = int(input("Birinchi tomonni kiriting"))
# b = int(input("ikkinchi tomonni kiriting"))
# c = int(input("Uchinchi tomonni kiriting"))

# if a + b > c and b + c > a and a + c > b:
#     print("Uchburchak yasab bo'ladi")
# else:
#     print("uchburchak yasab bo'lmaydi")
    
# 6-mashq
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# if a > b:
#     print(a)
# else:
#     print(a, b)

# 7-mashq
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# if a <= b:
#     a = 0
#     print(a, b)
# else:
#     print(a, b)

# 8-mashq
# import math
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# if a >= b >= c:
#     print(2 * a, 2 * b, 2 * c)
# else:
#     print(int(math.fabs(a)), int(math.fabs(b)), int(math.fabs(c)))

# 9-mashq
# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# a = 2 * x * 2 * y
# b = (x + y) / 2
# if x > y:
#     x = a
#     y = b
# else:
#     y = a
#     x = b

# print(x, y)

# 10-mashq
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# if a < b < c:
#     print("YES")
# else:
#     print("NO")

# 15, -5, 0, 104, 189, 89.77
# print(max(15, -5, 0, 104, 189, 89.77))
# print(min(15, -5, 0, 104, 189, 89.77))

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
# # print(max(x, y, z), min(x, y, z))
# a = max(x + y + z, x, y, z)
# b = min(x + y / 2, x, y, z) ** 2
# print("%.2f" % a, "%.2f" % b)

# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# if x < 0 and y < 0:
#     print(abs(x), abs(y))
# elif x < 0 or y < 0:
#     print(x + 0.5, y + 0.5)
# elif x > 0 and y > 0:
#     print(x, y)
# import math
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# D = b ** 2 - 4 * a * c
# if D > 0:
#     x1 = (- b + math.sqrt(D)) / (2 * a)
#     x2 = (- b - math.sqrt(D)) / (2 * a)
#     print("%.2f" % x1, "%.2f" % x2)
# elif D == 0:
#     x = - b / (2 * a)
#     print("%.2f" % x)
# else:
#     print("NO")

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2

# print(x, y, z)


# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# z = float(input("3-sonni kiriting: "))
# if 1 <= x <= 3:
#     print(x)
# if 1 <= y <= 3:
#     print(y)
# if 1 <= z <= 3:
#     print(z)

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# c = float(input("3-sonni kiriting: "))
# d = float(input("4-sonni kiriting: "))
# min_value = min(a, b, c, d)
# max_value = max(a, b, c, d)
# if a <= b <= c <= d:
#     a = b = c = d = max_value
# else: 
#     a = b = c = d = min_value

# print(a, b, c, d)

# homework
# x = float(input("1 chi sonni kiriting "))
# y = float(input("2 chi sonni kiriting "))
# g = (x + y) / 2
# h = 2 * x * y
# if x < y:
#     x = g
#     y = h
# elif x > y:
#     x = h
#     y = g

# print(x, y)

#
x = float(input("1-sonni kiriting: "))
y = float(input("2-sonni kiriting: "))
z = float(input("3-sonni kiriting: "))
min_value = min(x, y, z)
if x < 1 and y < 1 and z < 1:
    if min_value == x:
        x = (y + z) / 2
    elif min_value == y:
        y = (x + z) / 2
    else:
        z = (x + y) / 2
# else: 
#     x = x
#     y = y
#     z = z

print(x, y, z)