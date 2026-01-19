my_list = ['sanket',22,'asdf798',False]
print(type(my_list))

name = my_list[2]

print(name)

my_list[0] = 'Dedhia'

print(my_list)
my_list.append('Aditi')
my_list.pop()
my_list.remove(22)
my_list.insert(1,'Bro')

my_dict = {'name' : 'sanket', 'age' : 22, 'is_student' : False}

print(my_dict)

del my_dict['location']

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

x = (3,4)
x.append(5)
x.pop()

my_set = set(my_list)
print(my_set)
print(type(my_set))

scores = [56,78,90,34,90,22]
my_scores = set(scores)
print(my_scores)