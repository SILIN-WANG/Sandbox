out_file = open("name.txt","w")
name = input("What is your name?")
print(name, file=out_file)
out_file.close()


out_file = open("name.txt","r")
name = out_file.readline()
print("Your name is {}".format(name))
out_file.close()


out_file = open("number.txt","r")
num1 = int(out_file.readline())
num2 = int(out_file.readline())
print(num1+num2)
out_file.close()


out_file = open("number.txt","r")
total = 0
for i in out_file:
    numbers = int(i)
    total +=numbers
print(total)
out_file.close()

