# def add_numbers(a, b):
#     print(a + b)

# add_numbers(5, 10) # 15
# add_numbers(3, 7) # 10

# Qiymat qaytaruvchi funksiya
# return - funksiya ichida natija qaytarish uchun ishlatiladi
# def add_numbers(c, d):
#     return c + d

# print(add_numbers(8, 7)) # 15
# result = add_numbers(4, 6)
# print(result) # 10

# print("abc" * 5) # abcabcabcabcabc
# print("a" + 5)
# TypeError: can only concatenate str (not "int") to str
# print("a" / 5)
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print("5" - 5)
# TypeError: unsupported operand type(s) for -: 'str' and 'int'

# def isEven(number):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"
    
# print(isEven(4)) # Juft
# print(isEven(7)) # Toq

# Ternary operator yordamida qisqaroq yozish
def isEven(number):
    return "Juft" if number % 2 == 0 else "Toq"

print(isEven(4)) # Juft
print(isEven(7)) # Toq
