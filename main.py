# 1
# def gatesQuote(author):
#     quote = '''"Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
# {}'''
#     print(quote.format(author))
#
# gatesQuote("Bill Gates")
# 2
# def evenDigits(start, end):
#     for i in range(start, end + 1):
#         if i % 2 == 0:
#             print(i)
#
# start_num = int(input("Input start digit: "))
# end_num = int(input("Input end digit: "))
#
# evenDigits(start_num, end_num)
# 3
# def display_square(side_length, symbol, filled):
#     if filled:
#         for i in range(side_length):
#             print(symbol * side_length)
#     else:
#         for i in range(side_length):
#             if i == 0 or i == side_length - 1:
#                 print(symbol * side_length)
#             else:
#                 print(symbol + " " * (side_length - 2) + symbol)
#
# side = int(input("Input side lenght: "))
# symbol = input("Input symbol: ")
# is_filled = input("Input True, if square is filled, else input False: ").lower() == "true"
#
# display_square(side, symbol, is_filled)
# 4
# def minimalDigit(num1, num2, num3, num4, num5):
#     print(min(num1, num2, num3, num4, num5))
#
#
# num1 = int(input("Input number 1: "))
# num2 = int(input("Input number 2: "))
# num3 = int(input("Input number 3: "))
# num4 = int(input("Input number 4: "))
# num5 = int(input("Input number 5: "))
# minimalDigit(num1, num2, num3, num4, num5)

#5
# def multDigits(start, end):
#     if start > end:
#         start = end
#         end = start
#     else:
#         print(start * end)
#
#
# num1 = int(input("Input start digit: "))
# num2 = int(input("Input end digit: "))
# multDigits(num1, num2)

#6
# def quantDigits(num):
#     print(len(num))
#
# num = input("Input number: ")
# quantDigits(num)
#7
# def palindromDigit(number):
#     if number == str(number[::-1]):
#         print("True")
#     else:
#         print("False")
# num = input("Input number: ")
# palindromDigit(num)