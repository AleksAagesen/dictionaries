dict ={}
user_input = None
while user_input != 'revert':
    user_input = input('Type a input in this format: key;value ')
    if user_input == 'revert':
        for key_val in dict.items():
            print(key_val)

        dict2 = {value: key for key, value in dict.items()}
        for key_val in dict2.items():
            print(key_val)
    else:
        key, value = user_input.split(';')
        dict[key] = value

