# text = "Python lessons"
# print(len(text)) # 14
# string ichidagi har bir belgi indeksga ega (0 dan boshlanadi)
# print(text[0]) # P
# print(text[1]) # y
# print(text[2]) # t
# print(text[6]) # bo'shliq
# print(text[13]) # s
# print(text[-1]) # s
# print(text[-2]) # n
# string ichidagi oxirgi belgini olish uchun -1 indeksidan foydalanamiz
# print(text[-1]) # s
# print(text[len(text) - 1]) # s
# for sikl
# 1-usul:
# for belgi in text:
#     print(belgi)
# 2-usul:
# for index in range(len(text)):
#     print(index, text[index])

txt = "Bugun darsga Xursandbek kelmadi"
# in operatori yordamida string ichida ma'lum bir belgining bor yoki yo'qligini tekshirish
print("Xursandbek" in txt) # True
print("Asadbek" in txt) # False
print("y" in txt) # False
print("a" in txt) # True