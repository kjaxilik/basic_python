
def generator_file():    
    data_list = ['firm_1 РћРћРћ 10000 5000', 'firm_2 IP 14000 3000', 'firm_3 РћРћРћ 8000 90000', 'firm_4 IP 3000 8000']
    f_file_open = open('file_7.txt', 'w', encoding = 'utf-8')
    for i in range(len(data_list)):
        f_file_open.write(str(data_list[i]) + "\n") 
    f_file_open.close()    

generator_file()


with open('file_7.json', 'w', encoding = 'utf-8') as write_js:
    json.dump(profit, write_js, ensure_ascii=False)
    js_str = json.dumps(profit)
    print(f'РЎРѕР·РґР°РЅ С„Р°Р№Р» СЃ СЂР°СЃС€РёСЂРµРЅРёРµРј json СЃРѕ СЃР»РµРґСѓСЋС‰РёРј СЃРѕРґРµСЂР¶РёРјС‹Рј: \n '
          f' {js_str}')






import pandas as pd


class Auto:
    # атрибуты класса
    auto_name = "Lexus"
    auto_model = "RX 350L"
    auto_year = 2019

    # Методы класса
    def on_auto_start(self):
        print(f"Заводим автомобиль")

    def on_auto_stop(self):
        print("Останавливаем работу двигателя")



a = Auto()

print(a)
print(type(a))
print(a.auto_name)
a.on_auto_start()
a.on_auto_stop()

pd.read_csv('gg')



class Auto:
    # атрибуты класса
    auto_count = 0
    # методы класса
    def on_auto_start(self, auto_name, auto_model, auto_year):
        print("автомобиль заведен")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1

a = Auto()
a.on_auto_start("Lexus", "RX 350L", 2019)
print(a.auto_name)
print(a.auto_count)


a.on_auto_start("Lexus2", "RX 450L", 2020)
print(a.auto_name)
print(a.auto_count)


a_2 = Auto()
a_2.on_auto_start("Mazda", "CX 9", 2018)
print(a_2.auto_name)
print(a_2.auto_count)


pd.__version__


import numpy as np
np.__version__



class Auto:
    # атрибуты класа
    auto_count = 0
    def __version__(self):
        print('v0')
    # методы класса
    def __init__(self):
        Auto.auto_count += 1
        print(Auto.auto_count)

a_1 = Auto()
print(a_1.__version__)

a_2 = Auto()
a_3 = Auto()


class Auto: 
    def get_class_info(self):
        print("Р”РµС‚Р°Р»СЊРЅР°СЏ РёРЅС„РѕСЂРјР°С†РёСЏ Рѕ РєР»Р°СЃСЃРµ")

a = Auto()
a.get_class_info()




class Auto:  
    
    def on_start(self):
        info = "Автомобиль заведен"
        return info

a = Auto()
a.on_start()
a.info



class Auto:
   info_1 = "Автомобиль заведен"

   def on_start(self):
       self.info_2 = "Автомобиль заведен"

   def on_stop(self):
       info_3 = "Автомобиль stop"


a = Auto()
a.on_start()
a.on_stop()
print(a.info_2)
print(a.info_3)








class Auto:
    def metod1(self, p1, p2, p3):
        print("РђРІС‚РѕРјРѕР±РёР»СЊ Р·Р°РІРµРґРµРЅ")
        self.auto_name = p1 # в—Џ	Public (публичный).
        self._auto_year = p2 # в—Џ	Protected (защищенный).
        self.__auto_model = p3  # в—Џ	Private (приватный).
        

a = Auto()
a.metod1(p1='p1', p2='p2', p3='p3')
a.metod1(p1='p_1', p2='p_2', p3='p_3')

print(a.auto_name)
print(a._auto_year)
print(a._Auto__auto_model)

a.auto_name = 1
a._auto_year = 2
a._Auto__auto_model = 3



class MyClass:
    _attr = "значение"
    def _method(self):
        print("Это приватный метод!")

mc = MyClass()
mc._method()
print(mc._attr)


class MyClass:
    __attr = "значение"
    def __method(self):
        print("Это защищенный метод!")

mc = MyClass()
mc.__method()
print(mc.__attr)




class MyClass:
    __attr = "значение"
    def __method(self):
        print("Это защищенный метод!")

# можно просмотреть значение защищенного элемента
mc = MyClass()
mc._MyClass__method()
print(mc._MyClass__attr)






# Класс Transport
class Transport:
    count = 0
    def transport_method(self):
        print("Это родительский метод из класса Transport")

# Класс Auto, наследующий Transport
class Auto(Transport):
    def read_pdf(self):
        print("Это метод из дочернего класса")

a = Auto()
a.count
a.read_csv() # Вызываем метод родительского класса

a.read_csv()






# РєР»Р°СЃСЃ Auto
class Auto:
    def auto_start(self, param_1, param_2=None):
        if param_2 is not None:
            print(param_1 + param_2)
        else:
            print(param_1)


a = Auto()
a.auto_start(50)
a.auto_start(10, 20)








# класс Transport
class Transport:
    def _show_info1(self):
        print("Родительский медот класса Transport _")
    def __show_info2(self):
        print("Родительский медот класса Transport __")


# класс Auto, наследующий Transport
class Auto(Transport):
    def show_info(self):
        print("Наследующий метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def show_info(self):
        print("Наследующий метод класса Bus")


t = Transport()
t._show_info1()

a = Auto()
a._show_info1()
a.__show_info2()

b = Bus()
b.show_info()










