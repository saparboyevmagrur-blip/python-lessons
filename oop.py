# OOP - Object Oriented Programming
# 1. Class(properties, methods) va Object
# 2. OOP ustunlari
    # 1. Encapsulation
    # 2. Inheritance(Merosxo'rlik)
    # 3. Polymorphism 
    # 4. Abstraction

class Avtomobil:
    def __init__(self, rang, model):
        self.rang = rang
        self.model = model

    def yur(self):
        print(f"{self.model} yuryapti!")

# objects
car1 = Avtomobil("qora", "malibu")
car2 = Avtomobil("oq", 'cobalt')
car1.yur()
car2.yur()
print(type("test"))