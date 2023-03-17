num1 = int(input("Enter from which number you want to find the multiply: "))
num2 = int(input("Enter upto which number you want to find the multiply: "))
if num1>num2:
    num1,num2=num2,num1
for i in range (num1,num2+1):
    with open(f"multiplication table of {i}.txt", "w") as file:
        for j in range (1,11):
            p = (f"{i} x {j} = {i*j}\n")
            file.write(p)