def addtwo(a,b):
    return a + b
def multtwo(a,b):
    return a * b

print ("Hello World")
i = input("Enter an integer between 0-100: ")
i_int = int(i)
print("the number input was = ", i_int)
# add line to multiply and print input number
j = i_int * 2
print ("twice the input = ", j)
# another calc and print statement
k = j + j
k2 = addtwo(k,j)
mult2 = multtwo(k,j)
print ("k2 = ", k2, "  m2 = ", mult2)
print ("input value: ", i, "   four times the input value: ", k)
# read commandFile and print commands
print ("opening and reading commandFile")
file_name = 'commandFile.txt'
f = open(file_name, "r")
commands = f.readlines()
print ("Start read of command file")
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()
        print ("Next command: ", command)

# add another print line
print ("end of input phase")