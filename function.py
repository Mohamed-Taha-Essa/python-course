# price = 100 
# discount = price * 0.10
# final_price = price -discount
# print(final_price)

# price2 = 250 
# discount2 = price2 * 0.10
# final_price2 = price2 -discount2
# print(final_price2)
if False:
    def calculate_discount(price):
        discount = price * 0.10

        final_price = price - discount
        return final_price

    result = calculate_discount(100)
    print(result)
    result2= calculate_discount(price=90)
    print(result2)
    print(calculate_discount(250))


if False:
    def great():
        print('great')
    
    a = great
    print(a())


if False:
    def name(yourname): # yourname is a parameter
        print(yourname)

    name('ahmed') # ahmed is an argument

if 0 :
    def add(a, b):
        return a + b

    print(add(b=1, a=2))

if 0:
    def check_age(age):
        if age<0 :
            return 'invalid age'
        if age>=18:
            return 'adult man' 
        return 'Minor'
    
    print(check_age(-5))
    print(check_age(20))
    print(check_age(15))
if 0 : 
    def great(name='guest'):
        print(f'hello {name}')
        
    great()
    great('ahmed')

if 0 : 
    def calculate_shipping(weight ,rate=10):  
        print('rate : ' ,rate)  
        return weight * rate
    
    print(calculate_shipping(5))
    print(calculate_shipping(5, 20))

if 0 : 
    def create_profile(username ,age ,city):
        print(f"{username} , {age} ,from {city}")

    create_profile('ahmed' ,25 ,'ismailia')
    create_profile(age = 25 ,username='ali' ,city='ismailia')
    create_profile('ahmed' ,city='cairo' ,age=25)
    # create_profile(age=23 ,'ali' ,city ='mansoura')

if 0 : 
    def show_items(*item):
        print(type(item))
        for i in item:
            print(i)
        print(item)
    
    show_items(10, 20, 30, 40, 50)
    show_items(10)

if 0 :
    def show_details(**details):
        print(type(details))
        print(details)

    show_details(name='ali' , age=25 ,city='ismailia')

if 0: 
    def create_order(order_id , *items ,**extra_info):
        print(f"order ID : {order_id}")
        print(f"Items: {items}")
        print(f"Extra info: {extra_info}")

    create_order(1021 ,'ball' ,'shirt','shoes' ,customer='ahmed' ,shipping='express' ,city ='cairo')

if 0:
    def try_change(number):
        number = number+10
        print('inside: ',number)
    x = 5
    try_change(x)
    print('outside: ',x)


if 0 :
    def try_change(number):
        # number = number.copy()
        number.append(99)
        print('inside: ',number)
    x = [5,6]
    try_change(x)
    print('outside: ',x)

if 0: 
    def update_user(user):
        user['name'] = 'ahmed'
        user['age'] = 25
    
    profile={'name':'mohamed' , 'age':30 , 'city':'cairo'}
    update_user(profile)
    
    print(profile)

if 1 :
    c = 0 
    def add(a ,b):
        global c 
        c = a+b
        return c

    add(4 ,5)
    print(c)