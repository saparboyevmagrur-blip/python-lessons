# Function - ma'lum bir vazifani bajaradigan kod blokidir.
# Ularni qayta ishlatish mumkin va ular dastur tuzilishini yaxshilaydi.
# print(), range(), input(), list(), type()
# declaration(funksiyani e'lon qilish)
# def salom_ber():
#     print("Assalom alaykum!")

# call(funksiyani chaqirish)
# salom_ber()  # Funksiyani chaqirish
# salom_ber()  # Funksiyani yana bir marta chaqirish
# print("hey guys")

# FUNKSIYAGA QIYMAT UZATISH
# parametrlar.
# argumentlar.
# def salom_ber(ism):
#     print(f"Assalom alaykum, {ism}!")

# salom_ber("Ali")  # Funksiyani chaqirish
# salom_ber("Vali")
# salom_ber("Kumush")

# def yigindi(a, b):
#     print(a + b)

# yigindi(5, 10)  # 15
# yigindi(3, 7)   # 10

# default value
# def yosh_hisobla(ism = "Olim", tugilgan_yil = 1980):
#     yosh = 2026 - tugilgan_yil
#     print(f"{ism}ning yoshi: {yosh}")

# yosh_hisobla("Ismoil", 2000) # Ismoilning yoshi: 26
# yosh_hisobla("Gulbahor", 1995) # Gulbahorning yoshi: 31
# yosh_hisobla()
# yosh_hisobla("Jumagul", 1960)
# yosh_hisobla()

# def yosh_hisobla(tugilgan_yil, joriy_yil=2026):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
 
toliq_ism('olim', 'hakimov')