# Dictionary elementlari bilan ishlash
phone = {
    'brand': "Apple",
    "model": "iPhone 17 Pro Max",
    "color": "Silver",
    "storage": "256GB",
    "price": "$1500"
}

# get() metodi - kalit orqali qiymatni olish
print(phone.get("model"))  # iPhone 17 Pro Max
print(phone.get("price", "Narx topilmadi"))  # $1500
print(phone.get("battery")) # None, chunki 'battery' kaliti mavjud emas
print(phone.get("battery", "Kalit topilmadi"))  # Kalit topilmadi

# items() metodi - lug'at elementlarini (kalit, qiymat) juftlari sifatida olish
print(phone.items()) # dict_items([('brand', 'Apple'), ('model', 'iPhone 17 Pro Max'), ('color', 'Silver'), ('storage', '256GB'), ('price', '$1500')])
for key, value in phone.items():
    print(f"Kalit: {key}")
    print(f"Qiymat: {value}")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# keys() metodi - lug'atning barcha kalitlarini olish
print(phone.keys()) # dict_keys(['brand', 'model', 'color', 'storage', 'price'])
# print(telefonlar.keys()) # dict_keys(['ali', 'vali', 'olim', 'orif'])

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
}

print(mahsulotlar.keys())

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# in operatori
# 1. List elementlari orasida qiymatning mavjudligini tekshirish
# 2. Kalitning lug'atda mavjudligini tekshirish
bozorlik = ['anor','uzum','non','baliq', 'go\'sht', 'suv', 'shakar', 'tuxum']
# print("anor" in bozorlik) # True
# print("olma" in bozorlik) # False

# mahsulot = input("Qaysi mahsulotni sotib olmoqchisiz? ")
# if mahsulot in bozorlik:
#     print(f"{mahsulot.title()} do'konimizda bor.")
# else:
#     print(f"{mahsulot.title()} do'konimizda yo'q.")

# mahsulotlar bu lug'at
for mahsulot in mahsulotlar:
    # print(mahsulot) # mahsulotlar lug'atining kalitlari
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} do'konimizda bor.")
    else:
        print(f"{mahsulot.title()} do'konimizda yo'q.")

# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
print(mahsulotlar)
print(sorted(mahsulotlar)) # ['anjir', 'anor', 'olma', 'shaftoli', 'uzum']

print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# values() metodi - lug'atdagi qiymatlarni list sifatida olish
print(mahsulotlar.values()) # dict_values([10000, 20000, 40000, 25000, 30000])
print("Do'konimizdagi narxlar:")
for narx in mahsulotlar.values():
    print(narx)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
}

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)