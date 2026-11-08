# # set
# # {}
# # collection of data
# # unorderd
# # unindex
# # mutable
# # does not allow dupicate values

# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4}
# print(type(a))


# union kandu pidikan
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4}
# print(a.union(b))  # or a|b
# print(a.intersection(b))  # or a&b
# print(b-a)  # or a-b

# example

# fruits={"apple","banana","mango","grapes"}

# for i in fruits:
#     print(i)


# dictionary
# collection of data

# key:value pair

# data={"name":"abhinav","age":20,"location":"delhi"}
# for i in data:
#     print(i,data[i])


# reverse 
a= "abhinav"
rev=""
for i in range(len(a)-1,-1,-1):
    rev=rev + a[i]
print(rev)