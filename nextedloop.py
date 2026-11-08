# nested loops    pattern printing

# ivide nadakunne oro loop ahn (i,1+1,2+1,3+1)

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*",end="")


#     print()


# reverse pattern


# for i in range(5,0,-1):
#     for j in range(1, i+1):    j value koodunu or range koodunu
#         print("*",end="")


#     print()


# for pyramid shape space veran


# for i in range(1, 6):
#     for j in range(6 - i):
#         print(" ", end="")

#     for k in range(1, i + 1):
#         print(" ^ ", end="")

#     print()


for i in range(1,9):
    for j in range(9-1):
        if(i+j) % 2==0: 
            print("w",end=" ")
        else:
           print("B",end=" ")

    print()


    