month_short='feb'
month_long ='January'

months ={
    'jan': 'January',
    'feb': 'February',
    'mar': 'March',
    'apr': 'April',
    'may': 'May',
    'jun': 'June',
    'jul': 'July',
    'aug': 'August',
    'sep': 'September',
    'okt': 'Oktober',
    'nov': 'November',
    'dec': 'December'
}

for key in months:
    if key == month_short:
        print (months[key])

for key,value in months.items():
    if value == month_long:
        print(key)