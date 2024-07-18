age = input('How old are you? ')
print()
print(f'You are {age} years old.')

years = [10,20,30,40]
for i in years:
    print(f'In {i} years, you will be {int(age) + i} years old.')
