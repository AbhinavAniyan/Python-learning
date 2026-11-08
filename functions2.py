# check if a number amstring or not

def count(num):
    count=0
    while num>0:
        num=num//10
        count=count+1
    return count
