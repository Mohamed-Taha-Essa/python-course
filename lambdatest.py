# def square(x)->int:
#     return x**2

# print(square(5))

# square2 = lambda x : x**2
# print(square2(5))

# products = [('shoes ' , 54.25),('shirt ' , 58.25),('hat ' , 30.25),('dress ' , 66.25) ]
# products.sort(key= lambda item :item[1])
# print(products)

# def apply_operation(numbers , operation):
#     return [operation(n) for n in numbers]

# numbers = [1,2,5,6,9,8,4]
# result = apply_operation(numbers ,square)
# print(result)
#

def factorial(n):
    if n<=1 :
        return 1
    print(n)
    return n * factorial(n-1)



if __name__ == '__main__':
    print(__name__)
    print(factorial(5))
    print('hello from main')

else:
    print(__name__)
    print(__file__)
    print(__package__ or 'no package')
