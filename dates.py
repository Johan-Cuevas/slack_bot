import datetime
import calendar, time; 

class ConvertDate:

    def __init__(self, year=1980, month=1, day=1, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def check_year(self, year):
        try:
            int(self.year)
            return True
        except TypeError:
            return TypeError
        except ValueError:
            print("ValueError")
            return ValueError
        except TypeError:
            print("TypeError")
            return TypeError
        except:
            print("Some other error")
            raise EOFError

    def get_year(self):
        year = input("Enter the year here: ")
        if self.check_year(year) is True:
            print("Works if true")
            self.year = year
        else:
            print("works if false")
            self.year = self.year


# d = datetime.datetime(2020,12,30,17,0, 0).timestamp()
# print(d, "Time 5pm local time")

# print(calendar.timegm(time.strptime('2020-12-30 23:45:27', '%Y-%m-%d %H:%M:%S')))


# def get_time():
#     month = int(input("Enter the month here: "))
#     year = int(input("Enter the year here: "))
#     day = int(input("Enter the day here: "))
#     hour = int(input("Enter the hour here: "))
#     minute = int(input("Enter the minute here: "))
#     second = int(input("Enter the second here: "))
#     return datetime.datetime(year, month, day, hour, minute, second).timestamp()

# print(get_time())

convert_date = ConvertDate()
convert_date.get_year()
print(convert_date.year)
# get_year = get_input_date()