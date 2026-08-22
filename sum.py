def summition(a ,b):
    return a+b 


# print('__name__ = ', __name__)
# print(__file__)
# print(__package__ or '(no package)')


if __name__ == "__main__":
    print("This file is running directly")
    print(summition(5, 3))

else:
    print("This file is being imported")
    print("sum module name:", __name__)