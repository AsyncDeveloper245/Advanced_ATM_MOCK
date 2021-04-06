import random
courses = ['mts223','mts241','sts281','sts213','mts211']
days = 9
print('You want the time table to span a range of {} days'.format(days))
for i in range(days):
    #course = random.choice(courses)
    print(f'Course {random.choice(courses)} is scheduled for day {i+1}')
    #courses.remove(course)
