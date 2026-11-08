# scope means area in which is recognised

# name="abhinav"
# def name():
#     name="abhinav"
#     print(name)
# name()
# def nickname():
#      nickname="abhi"
#      print(nickname)    
# nickname()    


# x= 10  # global variable
# def times():
#     global x
#     x= x*2
#     print(x)
# times()
# print(x)    


# def times():
#     x= 10  # local variable
#     x= x*2
#     print(x)
# times()    


# args and kwargs

# def name(fname,lname,mname):
#     print(fname+" "+lname+" "+mname)
# name(fname="abhinav",lname="kumar",mname="singh")

# def name(*args):
#     print(args) 
# name("abhinav","kumar","singh","abhi","singh",)

# def name(**kwargs): recive in tuple
#     print(kwargs)
# name(fname="abhinav",lname="kumar",mname="singh")
# 

def name(*args,**kwargs):
    name=""
    for i in kwargs:
        name=name+kwargs[i]+" "
    print(name)
name(fname="abhinav",lname="kumar",mname="singh") 
