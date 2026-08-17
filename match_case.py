day = 'fri'

# if day == 'mon':
#     print('Monday')
# elif day == 'tue':
#     print('tuesday')
# else:
#     print('friday')

# match day:
#     case "mon":
#         print("monday")

#     case "tue":
#         print('tuesday')

#     case _:
#         print('unknown day')

# match day:
#     case "mon" | "sun":
#         print("work")

#     case "tue" | 'wed':
#         print('work')

#     case "fri" | 'sat':
#         print('weekend')

# status_code = 404
# match status_code:
#     case 200 :
#         print('Ok')
#     case 404 :
#         print('Not Found')
#     case 500:
#         print('Server Eror')
#     case _:
#         print('unknown status_code')
#
order_status = "shipped"

match order_status:
    case "pending":
        print("Your order is being prepared.")
    case "shipped":
        print("Your order is on its way.")
    case "delivered":
        print("Your order has arrived.")
    case "cancelled":
        print("Your order was cancelled.")
    case _:
        print("Unknown order status.")
