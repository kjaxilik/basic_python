# -*- coding: utf-8 -*-
'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) 
и метод running (запуск). Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, 
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

import time

class TrafficLight:
    
    def __running():
        colors = {'green': 7, 'yellow': 2, 'Red': 7, 'yellow': 2}
        for key, value in colors.items():
            # секундомер
            def secundomer(sec, color):
                while sec != 0:
                    print(color, ':', sec,'секунды')
                    time.sleep(1)
                    sec -= 1
            secundomer(value, key)
            # print(key, value)
t = TrafficLight
t._TrafficLight__running()
    

'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: 
length (длина), width (ширина). Значения данных атрибутов должны 
передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия 
всего дорожного полотна. Использовать формулу: 
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
depth = 5 # initial coverage depth (in sm)
mass_per_sq_m = 25 # initial mass per square meter (in kg)
'''

class Road:
    mass_per_sq_m = 25 # initial mass per square meter (in kg)
    depth = 5 # initial coverage depth (in sm)
    
    def __init__(self, lenght, width):
        self._length = length
        self._width = width
    
    def mass_total(self, depth):
        if depth != 1:
            return depth * self.mass_per_sq_m * self._width * self._length
        else:
            return self.mass_per_sq_m * self._width * self._length
    
    
length = 20
width = 5000
depth = 5

r = Road(length,width)
if depth != 5:
    r.depth = depth
    print(f'r.depth: {r.depth}')
    
    print(f'r.mass_total depth not 5: {r.mass_total(depth)}')
    
else:
    print(f'r.mass_total depth is 5: {r.mass_total(depth)}')


'''
3. Реализовать базовый класс Worker (работник), 
в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, 
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника 
(get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, 
 передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus} # суммируем доход с бонусами


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)# достаем данные из родительского класса
    
    def get_full_name(self):
        return print(f'Фамилия и имя сотрудника: {self.surname} {self.name}')
    
    def get_total_income(self):
        return print(f'Доход сотрудника: {sum(self._income.values())}')
    
worker1 = Position('Ivanov', 'Andres', 'React programmer', 55000, 1500)
worker2 = Position('Jaxilikov', 'Kairat', 'Data Scientist', 135000, 5500)

print(worker1.get_full_name()) # почему то выходит в принте после этой функции None, пока не нашел
print(worker1.get_total_income()) # после этой тоже
print(worker1._income)
print(worker2.get_full_name()) # после этой тоже
print(worker2.get_total_income()) # после этой тоже
print(worker2.position)
      
    
'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, 
PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать 
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите 
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов 
и также покажите результат.
'''



'''
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних 
класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод 
для каждого экземпляра.
'''



