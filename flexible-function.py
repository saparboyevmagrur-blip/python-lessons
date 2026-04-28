# return function
# def sum_list(lst):
#     s = 0
#     for number in lst:
#         s += number

#     return s

# print(sum_list([15, -5, 0, 8, 7]))

# flexible(moslashuvchan) function
# *args, **kwargs
# *args usuli
# def summa(*sonlar):
#     # print(sonlar) # (a, b, c, d, ...)
#     # print(type(sonlar)) # tuple
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son

#     return yigindi

# print(summa(8, 9, 12, -5, 89, 100))
# print(summa(7, -5, -2))

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello", "Emil", "Tobias", "Linus")

# def summa(x, y=7, *sonlar):
#     return x + y + sum(sonlar)

# print(summa(1, 7, 1, -5, -2))
# print(summa(2, 12))

# **kwargs usuli
def avto_info(kompaniya, model, **malumotlar):
    # print(malumotlar) # {'key': value}
    # print(type(malumotlar)) # dict
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model

    return malumotlar

print(avto_info("GM Uzbekistan", "Onix", rang='qora', yil=2025))
print(avto_info("Kia", "K5", rang='qizil', narh=35000))

def my_function(**kid):
  print(kid)
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Amaliyot
# 1.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def multiple(*numbers):
    result = 1
    for number in numbers:
       result *= number
    return result
print(multiple(1, 5, 6, 4, 5))
    
   
