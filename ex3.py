dict ={}
istrue = True
while istrue:
    user = input('Type a input in this format: key;value ')
    if user == 'revert':
        istrue = False
    else:
        key, value = user.split(';')
        dict[key] = value

for key_val in dict.items():
    print(key_val)

dict2 = {value: key for key, value in dict.items()}
for key_val in dict2.items():
    print(key_val)