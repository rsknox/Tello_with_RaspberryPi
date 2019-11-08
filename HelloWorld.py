def addtwo(a,b):
    return a + b

print ("Hello World")
i = input("type integer: ")
i_int = int(i)
print("the number input was = ", i_int)
# add line to multiply and print input number
j = i_int * 2
print ("twice the input = ", j)
# another calc and print statement
k = j + j
k2 = addtwo(k,j)
print ("k2 = ", k2)
print ("input value: ", i, "   four times the input value: ", k)
# add another print line
print ("end of input phase")