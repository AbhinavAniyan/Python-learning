# # functions

# # def function(parameters):
# #     code to be executed


# def hello():
#     print("my name is abhinav")


# hello()   # calling the function
# hello()
# hello()

# def add(a=0,b=0):
#     print(a+b)

# add(2,5)

# def add(a=0,b=0):
#     print(a+b)

# def mul(x,y,z):
#     pass
# mul(x=1,y=2,z=3)
    
# add()


# def factorial(num):
#     fact=1

#     for i in range(1,num+1):
#         fact*=i
#     print(fact)    
# factorial(10)
# factorial(7)

# write a fnction to check if a string is unique or not

# def is_unique(string):
#     unique= True   
#     for i in range(0,len(string)):
#        for j in range(i+1,len(string)):
#            if string[i]==string[j]:
#                unique=False

#     if unique:
#         print("true")
#     else:   
#         print("false")               

# is_unique("abhinav")



# lambda functions

# def sum(a,b):
#     return a+b
# print(sum(2,3))
# b=lambda a,b:a+b
# # print(b(2,3))

# Ab= lambda n: n**2
# print(Ab(10))


# recursion
# to go back recur   function calling itself

# def countzero(n):
#     if n==1:
#         return 1    
#     return n * countzero(n-1) 

# print(countzero(10))   

