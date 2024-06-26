from address import Address
from mailing import Mailing
to_address = Address("432029", "Ульяновск", "Корунковой", "2", "360")
from_address = Address("400100", "Москва", "Фруктовая", "62", "45")
mailing = Mailing(to_address, from_address, 635, "880020006")
print(f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.')