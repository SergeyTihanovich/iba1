import unittest
from Airline import Aircraft

class Test_Airlines(unittest.TestCase):
    def test_get_flightnumber_targetPoint(self):
        """Проверяет правильность номера рейса."""
        test_flightnumber = 99999
        self.assertEqual(Aircraft.get_flightnumber_targetPoint('Vancouver'), test_flightnumber)
        # метод assert проверяет соответствие номера рейса выбранному направлению


    def test_period_needed(self):
        """Проверяет правильность данных о рейсе."""
        requestedWeekday="Monday"
        startTime = "2022-03-10"
        finishTime = "2022-04-01"


        test_flyDates = ['2022-03-14', '2022-03-21', '2022-03-28']
        for test_flyDate in test_flyDates:
            self.assertIn(test_flyDate, Aircraft.period_needed(startTime, finishTime, requestedWeekday))
          # метод assert проверяет соответствие даты рейса выдаваемого методом и верного результата


if __name__ == '__main__':
    unittest.main()
