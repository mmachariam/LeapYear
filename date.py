class DateCalculator:


    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    def get_weekday(self):
        if self.month <3:
             m = self.month + 12
             Y = self.year - 1
        else:
            m = self.month
            Y = self.year

        q = self.day
        K = Y  % 100 # year of the century
        J = Y // 100 # zero-based century

        h = (q + (13 *(m + 1)) // 5 + K + (K // 4) + (J // 4) + 5*J) %7



        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ]
        return days[h]

date = DateCalculator(1200,4,6)
print(date.get_weekday())

