my_dict ={
    'name': 'John',
    'Age': 30,
    'City': 'New York'
}
my_dict['salary'] = 50000

age = my_dict['Age']
print(age)

for i in my_dict.keys():
    print(f'key: {i}')

for i in my_dict.values():
    print(f'value: {i}')

for key_val in my_dict.items():
    print(f'info: {key_val}')

my_dict_2 = {value: key for key, value in my_dict.items()}
for key_val in my_dict_2.items():
    print(f'info: {key_val}')

my_dict_3 = {key: '0' for key in my_dict.items()}
for key_val in my_dict_3.items():
    print(f'info: {key_val}')

my_dict5 = {}

for data in [my_dict, my_dict_3]:
    my_dict5.update(data)

for key_val in my_dict5.items():
    print(f'info: {key_val}')