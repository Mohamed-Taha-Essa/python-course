# try :
#     age = int(input('enter your age '))

#     print(f'next year you will be {age +1}')
# except ValueError:
#     print('that is not valid number')


# try :
#     number = int(input('enter a  number : '))
#     result = 100/ number
#     print(result)
# except ValueError:
#     print('that is not valid number')
# except ZeroDivisionError:
#     print("you can't divide by zero ")


# try :
#     number = int(input('enter a  number : '))
#     result = 100/ number
#     print(result)

# except Exception as e :
#     print('the error is : ' ,e)

# # import pandas as pd

## else and finally
#
# try :
#     number = int(input('enter a  number : '))
# except ValueError:
#     print('invalid number ')
# else:
#     print('you entered : ' , number)

try :
    number = int(input('enter a  number : '))
    result = 10/number
    print(result)
except ValueError:
    print('invalid number ')
finally:
    print('you entered : ' , number  ,'and the program is finished')
