# decorators means function which enhance other function


# def saymyname(fun):
#     def wrapper():
#         print("say my name")
#         fun()
#         print("right...")
#     return wrapper

# @saymyname


# def greet():
#     print('hisenberg')
# greet()


# def saymyname(fun):
#     def wrapper(*args,**kwargs):
#         print("say my name")
#         fun(*args, **kwargs)
#         print("right...")
#     return wrapper


# @saymyname


# def greet(name):
#     print(f"hello{name}")


# @saymyname
# def greet(name):
#       print(f"hello{name}")


# @saymyname
# def addz(a,b):
#       print(a+b)


# greet("abhinav")
# addz(5,7)


# time

# import time
# # print(time.time()) ishtam olle time kandupidikan  
# # print(time.ctime()) current time kandupidiakn
# print(time.ctime(1793004504.0559661))  # epoch time  

# start= time.time()
# for i in range(1,6):
#     print(i)
#     time.sleep(1)     #sleep ,means seconds
# end = time.time()
# print("total time",end-start)

import time


    

def saymyname(fun):
    def wrapper(*args,**kwargs):
        print("say my name")
        fun(*args, **kwargs)
        print("right...")
    return wrapper


@saymyname


def greet(name):
    print(f"hello{name}")


@saymyname
def greet(name):
      print(f"hello{name}")


@saymyname
def addz(a,b):
      print(a+b)


greet("abhinav")
addz(5,7)

def ntimes(n):
     for i in range(0,n):
            print(i)
            time.sleep(1)
ntimes(10)
    