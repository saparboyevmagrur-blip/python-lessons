# 127
# numbers = [46, 23, -52, 34, 6, -18, 52]
# plan:
# 1. eng kichik element = min
# 2. manfiy elementlarini topish
# 3. m.elementlarini min ** 2 ga almashtirish => numbers[2] = 23
# min_value = min(numbers)
# for index in range(len(numbers)):
#     if numbers[index] < 0:
#         numbers[index] = min_value ** 2

# print(*numbers)

# 110
# nums = [7, 11, 83, 18, 31]
# K = int(input("K sonini kiriting: "))
# M = int(input("M sonini kiriting: "))
# k = 1
# for son in nums:
#     if son == K or son == M:
#         k *= son
# print(k) 

# 104
# plan:
# 1. min element topish
# 2. oxirgi element topish
# 3. almashtirish
sonlar = [74, 0, 1, 33] 
minimum_value = min(sonlar)
last_element = sonlar[-1]
min_index = sonlar.index(minimum_value)

sonlar[min_index] = last_element
sonlar[-1] = minimum_value
print(sonlar)