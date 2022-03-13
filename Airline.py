import calendar
import datetime


def __del__():
    pass


class Aircraft:
    """Базовый класс для всех пользователей"""

    TOTAL_OBJECTS=0

    # конструктор / динамические поля / магический метод
    def __init__(self, targetPoint, flightnumber, aircraft_type, flyWeekday, flyTime, startTime=None, finishTime=None):
        self.targetPoint = targetPoint
        self.flightnumber = flightnumber
        self.aircraft_type = aircraft_type
        self.flyWeekday = flyWeekday
        self.flyTime = flyTime
        self.startTime = startTime
        self.finishTime = finishTime
        Aircraft.TOTAL_OBJECTS = Aircraft.TOTAL_OBJECTS + 1


    def change_flightnumber(self, newflightnumber):
        self.flightnumber=newflightnumber
        return self.flightnumber

    def displayFlight(self):
        return print(
            'targetPoint:', self.targetPoint, '\n',
            'flightnumber: ', self.flightnumber, '\n',
            'aircraft_type:', self.aircraft_type, '\n',
            'flyWeekday :', self.flyWeekday , '\n',
            'flyTime :', self.flyTime , '\n',
                   )

    # функции-члены реализуют запись и считывание полей (проверка корректности)
    # для инкапсулированного поля
    def set_flynumber(self, flightnumber):
        if flightnumber > 0:
            self.__flighnumber = flightnumber
        else:
            print("flynumber не может быть отрицательным или нулевым!")

    # для открытого поля
    def set_Weekday(self, *Weekday):
        for weekday in Weekday:
            if weekday == '':
                self.Weekday = weekday
        else:
            print("Введите день недели в словом например Monday ")

    # обычный метод для вывода вариантов вылета в запрошенный период

    def period_needed(startTime, finishTime, requestedWeekday):
        start_date = datetime.datetime.strptime(startTime, '%d/%m/%Y')
        finish_date = datetime.datetime.strptime(finishTime, '%d/%m/%Y')
        print('_____All possible flights for the requested period:________')
        for i in range((finish_date - start_date).days):
            flyDate = datetime.datetime.date(start_date + datetime.timedelta(days=i))
            period = calendar.day_name[(start_date + datetime.timedelta(days=i + 7)).weekday()]
            if period == requestedWeekday:
                print(period)
                print(flyDate, '\n')

        return period

        # статический метод для вывода списка рейсов

    @staticmethod
    def get_flightnumber_targetPoint(targetPoint):
        if targetPoint == 'Warshaw':
            return print('33333')
        if targetPoint == 'Vancouver':
            return print('99999')
        if targetPoint == 'Varna':
            return print('88888')

# метод класса
    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)

#  Унаследуем класс Aircraft в дочерний класс ChildClass и объявим там переменную TOTAL_OBJECTS :
class ChildClass(Aircraft):
            TOTAL_OBJECTS = 0
            pass



if __name__ == '__main__':
    # реализация метода period_neded
    print('Реализация метода period_needed - после введения запрошенного периода выдается день недели и дата вылета: ',
          '\n')
    Aircraft.period_needed("12/03/2022", "01/04/2022", "Monday")

    # создание 2-x объектов экземпляров класса
    first_aircraft = Aircraft('Vienna', 11111, 'Boing747', 'Tuesday', '5.45')
    second_aircraft = Aircraft('Frankfurt', 22222, 'Boing777', 'Friday', '10.05')

    # Вызываем classmethod
    print('Вызываем classmethod :')
    Aircraft.total_objects()    # получаем количество объектов 2
    print('\n')

   # Вызовем метод класса total_objects(cls) из дочернего класса, он вернет общее количество объектов (ноль) для дочернего класса
    ChildClass.total_objects()
    print('@classmethod используется в суперклассе для определения того, как метод должен вести себя, когда он вызывается разными дочерними классами')
    print('\n')

    # доступ к полям созданных экземпляров:
    print('доступ к полям созданных экземпляров first_aircraft  and  second_aircraft:')
    print(first_aircraft.targetPoint)
    print(second_aircraft.flyTime)
    print(first_aircraft.aircraft_type)  # получаю доступ к полю aircraft_type созданного объекта first_aircraft
    print(second_aircraft.flightnumber,'\n')  # получаем доступ к полю flightnumber и 22222 на печати
    print('Теперь воспользуемся методом chang_flynumber и заменим номер вылета на 21112 в экземпляре second_aircraft :' )
    second_aircraft.change_flightnumber(21112)
    print('Получаем новый номер рейса :',second_aircraft.flightnumber, '\n')

    # реализация статического метода get_flynumber_targetPoint
    print("____________Реализация статического метода get_flynumber_targetPoint :_________________")
    Aircraft.get_flightnumber_targetPoint('Vancouver')
    print('Передали методу имя города а он вернул номер рейса \n')

    #реализация метода displayFlight
    print('_______Получим полную информацию о рейсе объекта second_aircraft с помощью метода displayFlight :')
    second_aircraft.displayFlight()


    # метод для изменения представления экземпляра класса / магический метод

    # создание 5 объектов класса
    print('___________создание списка объектов______________')
    Aircraft.target_point = [Aircraft('Viena', 11111, 'Boing747', 'Tuesday', '5.45'),
                             Aircraft('Frankfurt', 22222, 'Boing777', 'Friday', '10.05'),
                             Aircraft('Warshaw', 33333, 'Boing767', 'Monday', '15.40'),
                             Aircraft('Vancouver', 99999, 'Boing777', 'Saturday', '8.05'),
                             Aircraft('Varna', 88888, 'Boing747', 'Sunday', '12.50')]
    print(Aircraft.target_point, '\n')  # выдаст список созданных объектов

    print('___________выведем первый объект из созданного списка объектов______________')
    print(Aircraft.target_point[0], '\n')

       # _______________вывод строки документации класса с помощью магического метода __doc__
    print('вывод строки документации класса с помощью метода __doc__ ')
    print('Aircraft.__doc__', Aircraft.__doc__, '\n')

    # _______________вывод словаря класса с помощью магического метода __dict__
    print('вывод словаря класса с помощью метода __dict__ ')
    print('Aircraft.__dict__', Aircraft.__dict__, '\n')

    # _______________вывод имени класса с помощью магического метода __name__
    print('вывод имени класса с помощью метода __name__ ')
    print('Aircraft.__name__', Aircraft.__name__, '\n')

    # _______________вывод строки документации класса с помощью магического метода __module__
    print('вывод имени модуля, в котором определяется класс с помощью метода __module__ ')
    print('Aircraft.__module__', Aircraft.__module__, '\n')

    #_______________вызываем метод проверки правильности введения номера полета set_flynumber
    print('вызываем метод проверки правильности введения номера полета set_flynumber :')
    second_aircraft.set_flynumber(0)    # результат :flynumber не может быть отрицательным или нулевым!
    print('\n')

    # _______________вызываем метод set_Weekday для проверки правильности введения дня недели__________
    print('вызываем метод set_Weekday для проверки правильности введения дня недели:')
    first_aircraft.set_Weekday(1)

    __del__()

