#A program that generates a time table based on the data provided
import random
class TimeTableGenerator:
    def __init__(self):
        self.course_table = {}

    def setup_table(self, days_length, courses=[]):
        """This Function accepts a list-->courses and an integer-->days_length as parameters"""
        try:
            days = [x for x in range(days_length)]
            courses_list = random.shuffle(courses)
            for value in range(len(days)):
                self.course_table['day '+ value] = courses_list[value]
        except TypeError:
            print('Invalid Input')
    def get_table(self):
        return self.course_table

newTimeTable = TimeTableGenerator()

print(newTimeTable.setup_table(7,['mts223','mts241','sts281','sts213','mts211']))
print(newTimeTable.get_table())