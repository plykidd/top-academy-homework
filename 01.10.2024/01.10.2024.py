#
# # Задание 1
# #  Создайте класс Device, который содержит информа
# # цию об устройстве.
# #  С помощью механизма наследования,реализуйте класс  CoffeeMashine
# # (содержит информацию о кофемашине)
# # класс Blender (содержит информациюоблендере),класс
# # MeatGrinder (содержит информацию о мясорубке).
# #  Каждыйизклассов должен содержать необходимые
# # для работы методы.
#
#
# class Device:
#     def __init__(self, name, model, manufacturer):
#         self.name = name
#         self.model = model
#         self.manufacturer = manufacturer
#
#     def __str__(self):
#         return f'{self.name}, {self.model}, {self.manufacturer}'
#
#
# class CoffeeMachine(Device):
#     def __init__(self, name, model, manufacturer, coffee_type):
#         super().__init__(name, model, manufacturer)
#         self.coffee_type = coffee_type
#
#     def working(self):
#         return print('Coffee is working')
#
#     def __str__(self):
#         return f'{self.name}, {self.model}, {self.manufacturer}, {self.coffee_type}'
#
#
# class Blender(Device):
#     def __init__(self, name, model, manufacturer, color):
#         super().__init__(name, model, manufacturer)
#         self.color = color
#
#     def working(self):
#         return print('Blender is working')
#
#     def __str__(self):
#         return f'{self.name}, {self.model}, {self.manufacturer}, {self.color}'
#
#
# class MeatGrinder(Device):
#     def __init__(self, name, model, manufacturer, meat):
#         super().__init__(name, model, manufacturer)
#         self.meat = meat
#
#     def working(self):
#         return print('MeatGrinder is working')
#
#     def __str__(self):
#        return f'{self.name}, {self.model}, {self.manufacturer}, {self.meat}'
#
# coffeemachine = CoffeeMachine('Coffee Machine', 20, 'Raspberry Pi', 'Raspberry Pi')
# blender = Blender('Blender', 20, 'Raspberry Pi', 'Raspberry Pi')
# meatgrinder = MeatGrinder('Meat Grinder', 20, 'Raspberry Pi', 'Raspberry Pi')
#
# coffeemachine.working()
# blender.working()
# meatgrinder.working()



#  Задание 2
#  СоздайтеклассShip,которыйсодержитинформацию
# о корабле.
#  С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
#  Каждыйизклассов должен содержать необходимые
# для работы методы

# class Ship:
#     def __init__(self, name, speed, manufacturer):
#         self.name = name
#         self.speed = speed
#         self.manufacturer = manufacturer
#
#     def __str__(self):
#         return f'Ship: {self.name}, {self.speed}, {self.manufacturer}'
#
#
# class Frigate(Ship):
#     def __init__(self, name, speed, manufacturer, frigate_type):
#         super().__init__(name, speed, manufacturer)
#         self.frigate_type = frigate_type
#
#     def drive(self):
#         return print(f'Frigate {self.frigate_type}')
#
#     def __str__(self):
#         return f'{self.frigate_type}, {self.speed}, {self.manufacturer}'
#
#
# class Destroyer(Ship):
#     def __init__(self, name, speed, manufacturer, destroy_type):
#         super().__init__(name,speed, manufacturer)
#         self.destroy_type = destroy_type
#
#     def drive(self):
#         return print(f'Destroyer {self.destroy_type}')
#
#     def __str__(self):
#         return f'{self.name}, {self.speed}, {self.manufacturer}, {self.destroy_type}'
#
#
# class Cruiser(Ship):
#     def __init__(self, name, speed, manufacturer, cruiser_type):
#         super().__init__(name,speed, manufacturer)
#         self.cruiser_type = cruiser_type
#
#     def drive(self):
#         return print(f'Cruiser {self.cruiser_type}')
#
#     def __str__(self):
#         return f'{self.name}, {self.speed}, {self.manufacturer}, {self.cruiser_type}'
#
# frigate = Frigate('gsdgdsg', '2000', 'germany', 'frigate')
# destroyer = Destroyer('gsdgdsg', '2000', 'germany', 'destroyer')
# cruiser = Cruiser('gsdgdsg', '2000', 'germany', 'cruiser')
#
# frigate.drive()
# destroyer.drive()
# cruiser.drive()


# Задание 3
#  Запрограммируйте класс Money (объект класса опе
# рирует одной валютой) для работы с деньгами.
#  Вклассе должны бытьпредусмотрены поле для хра
# нения целойчастиденег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
#  Реализовать методы для вывода суммы на экран, за
# дания значений для частей.


# class Money:
#     def __init__(self, money, cent):
#         self.money = money
#         self.cent = cent
#
#     def __str__(self):
#         while self.cent > 100:
#             self.money += 1
#             self.cent -= 100
# 
#         return f'Money: {self.money}, Cent: {self.cent}'
#
#
# print(Money(100, 970))