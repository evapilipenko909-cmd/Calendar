import datetime

class CustomDate(datetime.date):
    # (наследуется от datetime.date)

    def __new__(cls, year=None, month=None, day=None):
        # cозд нового объекта дат
        # если не передали дату, берём сейчас
        if year is None or month is None or day is None:
            now = datetime.datetime.now()
            year = now.year
            month = now.month
            day = now.day

        # datetime.date неизменяемый, поэтому используем __new__
        instance = super().__new__(cls, year, month, day)
        return instance

    def get_string(self, format_str="%d.%m.%Y"):
        return self.strftime(format_str)

    def get_weekday_name(self, lang="ru"):
        weekdays_ru = ["Понедельник", "Вторник", "Среда", "Четверг",
                       "Пятница", "Суббота", "Воскресенье"]
        weekdays_en = ["Monday", "Tuesday", "Wednesday", "Thursday",
                       "Friday", "Saturday", "Sunday"]

        weekday_num = self.weekday()  # 0-6

        if lang == "ru":
            return weekdays_ru[weekday_num]
        else:
            return weekdays_en[weekday_num]

    def get_month_name(self, lang="ru"):
        months_ru = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                     "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        months_en = ["January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November", "December"]

        # self.month возвращает 1-12, а в списке индексы 0-11
        month_index = self.month - 1

        if lang == "ru":
            return months_ru[month_index]
        else:
            return months_en[month_index]

    def add_days(self, days):
        # используем timedelta для добавления дней
        new_date = self + datetime.timedelta(days=days)
        # возвращаем новый объект CustomDate
        return CustomDate(new_date.year, new_date.month, new_date.day)

    def add_months(self, months):
        # считаем новый месяц и год
        new_month = self.month + months
        new_year = self.year

        while new_month > 12:
            new_month = new_month - 12
            new_year = new_year + 1

        while new_month < 1:
            new_month = new_month + 12
            new_year = new_year - 1

        # проверяем, существует ли такой день в новом месяце, 31 февраля не существует
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #  на високосный год
        if new_year % 4 == 0 and (new_year % 100 != 0 or new_year % 400 == 0):
            days_in_month[1] = 29  # февраль 29 дней

        # если день больше макс, берём последний день месяца
        new_day = self.day
        if new_day > days_in_month[new_month - 1]:
            new_day = days_in_month[new_month - 1]

        return CustomDate(new_year, new_month, new_day)

    def __str__(self):
        return self.get_string()