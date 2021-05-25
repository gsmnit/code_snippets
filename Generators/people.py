import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f'Memory (Before): {mem_profile.memory_usage_psutil()}Mb')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.process_time()
# people = people_list(100000000)
# t2 = time.process_time()

t1 = time.process_time()
people = people_generator(100000000)
t2 = time.process_time()

print(f'Memory (After) : {mem_profile.memory_usage_psutil()}Mb')
print(f'Took {t2-t1} Seconds')
