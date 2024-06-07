catalog = []
    
from smartphone import Smartphone

# Создаем экземпляры класса Smartphone
phone1 = Smartphone("Samsung", "Galaxy S21", "+79111111111")
phone2 = Smartphone("Apple", "iPhone 12", "+79111111111")
phone3 = Smartphone("Xiaomi", "Redmi Note 10", "+79000000000")
phone4 = Smartphone("Google", "Pixel 5", "+79000000000")
phone5 = Smartphone("OnePlus", "8T", "+79555555555")

# Добавляем экземпляры в каталог
catalog.extend([phone1, phone2, phone3, phone4, phone5])

# Печатаем каталог
for phone in catalog:
   print(phone.brand,phone.model,phone.phone_number)


