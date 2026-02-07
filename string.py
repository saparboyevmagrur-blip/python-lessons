# String - matn
# Data types(Ma'lumot turlari)
# 1. string(matn) 2. number(son) => 1. integer(butun son) 5 -5 0 2. float(o'nlik son) 2.5 5.78 -83.99
# 3. boolean(mantiqiy qiymat) => 1. true(haqiqat); 2. false(yolg'on) 
username = "adminjon" # string
favourite_number = 77 # int
is_student = True # boolean

text = "Men yangi 📱 sotib oldim 😁😁 🏳️"
print(text)

city = "Shovot"
region = "Xorazm"
street = "Al-Xorazmiy" 
home_number = 34

# Matnlarni birlashtirish
# Men Xorazm viloyati Shovot shahri Al-Xorazmiy ko'chasi 34-uyda yashayman

# 1-usul: + operator yordamida
full_address = "Men " + region + " viloyati " + city + " shahri " + street + " ko'chasi " + str(home_number) + "-uyda yashayman."
print(full_address)

# 2-usul: f-string yordamida
address = f"Men {region} viloyati {city} shahri {street} ko'chasida yashayman."
print(address)

# Maxsus belgilar
print('Hello World!')
print('Hello \tWorld!') # t - tab
print('Hello \nWorld!') # n - new line

firstname = "Asadbek"
lastname = "Rakhimov"
# "Mening to'liq ism familyam: Asadbek Rakhimov"
fullname1 = f"Mening to'liq ism familyam: {firstname} {lastname}"
print(fullname1)
fullname2 = "Mening to'liq ism familyam " + firstname + ' ' + lastname
print(fullname2)