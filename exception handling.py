

# try:

#     a=5
#     b=0
#     print(a/b)
# except:
#     print("Error: Division by zero is not allowed.")
#     print("abhinav")


# try:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))

#     print(a/b)
# except:
#     print("Error")
# print("abhinav")


# try:
#     a = int(input("enter a number:"))
#     b = 6
#     print(a/b)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("check your values")
# except typeError:
#     print("check your type")
# finally:
#     print("always")

Exception
class age_error(Exception):
    pass    
age=14
if age < 18:
    raise age_error("age should greater than 18")