from address import Address
from mailing import Mailing

# Создаем экземпляр класса Address для адресов
to_address = Address("123456", "Москва", "Ленинская", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Невский", "5", "12")

# Создаем экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 500, "ABC123")

# Выводим информацию о почтовом отправлении
print("Отправление", mailing.track , "индекс",to_address.index, "город",to_address.city, "улица",to_address.street,"дом", to_address.house ,"квартира", to_address.apartment , from_address.index, from_address.city, from_address.street, from_address.house ,from_address.apartment,"Стоимость рублей.", mailing.cost)
