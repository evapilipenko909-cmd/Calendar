import calendar
import datetime

calendar_output = calendar.month(2026, 7)
print(type(calendar_output))
print(calendar_output)

#      July 2026
#Mo Tu We Th Fr Sa Su
#       1  2  3  4  5
# 6  7  8  9 10 11 12
#13 14 15 16 17 18 19
#20 21 22 23 24 25 26
#27 28 29 30 31

today = datetime.date.today()
days_matrix = calendar.monthcalendar(today.year, today.month)
print(days_matrix)

def day_matrix_to_day_list(matrix:list[list[int]], mode='simple') -> list[int]:
    """This function convert matrix with 2 methods"""
    days = []
    if mode:
        for item in matrix:
            for day in item:
                days.append(day)
        return days
    else:
        return [day for week in matrix for day in week]
    
print("simple way:",day_matrix_to_day_list(days_matrix))
print("list generator:",day_matrix_to_day_list(days_matrix, ""))


########################

print("week headers:", calendar.weekheader(2).split())