# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[0][0] )
# print(fruits[1][0] )
# print(fruits[2][0] )
# print(fruits[-1])
# for fruit in fruits:
#     for i in range(1):
#         print(fruit[i])


# for i in range(len(fruits)):
#     print(fruits[i][0])

# numbers = [10, 20, 30, 40, 50]

# print(numbers[1:3])   # [20, 30]
# print(numbers[:2])    # [10, 20]
# print(numbers[2:])    # [30, 40, 50]
# print(numbers[::-1])  # [50, 40, 30, 20, 10]  → reversed
# numbers[0]= 35
# print(numbers)

# numbers.append('ball')
# print(numbers)

# cart = []
# cart.append('mobile')
# cart.append('hat')
# print(cart)
#

cart = ['shoes']
cart_2 = ['shirt' , 'hat']
cart.extend(cart_2)
print(cart)
cart = ['shoes']
cart_2 = ['shirt' , 'hat']
cart.append(cart_2)
print(cart)
