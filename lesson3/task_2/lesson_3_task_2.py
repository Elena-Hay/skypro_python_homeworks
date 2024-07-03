from smartphone import Smartphone


catalog = []
tel_1 = Smartphone("Huawei", "nova 11 Pro", "+79055556677")
tel_2 = Smartphone("Samsung", "Galaxy A54 5G", "+79056596670")
tel_3 = Smartphone("ASUS", "Zenfone 10", "+79179999351")
tel_4 = Smartphone("Honor", "90", "+79183567239")
tel_5 = Smartphone("POCO", "F5 Pro", "+79063457211")
catalog.append(tel_1)
catalog.append(tel_2)
catalog.append(tel_3)
catalog.append(tel_4)
catalog.append(tel_5)
for tel in catalog:
    print(f'{tel.brand} - {tel.model}. {tel.tel_number}')