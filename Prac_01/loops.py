for i in range(0, 110, 10):
    print(i, end=" ")

for j in range(21, -1, -1):
    print(j,end=" ")

x = int(input("How many stars do you want?"))
for i in range(x):
    print("* "*(i+1))
