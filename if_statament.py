# age = input('enter your age ')
# age = int(age)
# if age>=18 :
#     print('you are adult.')
# else:
#     print('you are a minor .')

# score = 80
# gender = 'male'

# if score >= 90 :
#     print('grade A')

# elif score >= 80 :
#     print('grade B')

# elif score >= 70 :
#     print('grade C')
# else :
#     print('grade D')

# if gender =='male':
#     print(' you and mr')
# else:
#     print('you are mrs')

###########Nested Condition ##########
# age = 34
# has_id = False

# if age >=18:
#     if has_id:
#         print('Entry allowed')

#     else:
#         print('You need an Id')

# else:
#     print('you are too young')

###########  and or
# if age >=18 and has_id:
#      print('Entry allowed')
# else:
#     print('entry not allowed')


# weekend =False
# holiday = False

# if weekend or holiday:
#     print('No work today ')
# else:
#     print('you must work today')

# ternary expression
age = 18

status = "adult" if age >= 18 else 'minor'
print(status)
