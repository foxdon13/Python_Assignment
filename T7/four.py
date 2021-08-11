"""The quetsion did not mention anything about implementing the datetime module of the 
python class hence, the time was not initiated using the python's date time module"""


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def displaytime(self):
        print(f"{self.hours} hour and {self.minutes} minute")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{ total_minutes} ")

    def addTime(self, other):
        print(
            f"{self.hours+other.hours} hours and {self.minutes +other.minutes} minutes"
        )


time1 = Time(4, 5)
time1.displaytime()
time2 = Time(4, 5)
time1.addTime(time2)
