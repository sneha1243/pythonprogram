num1=int(input("enter the first no"))
num2=int(input("enter the second no"))
num3=int(input("enter the third no"))
if num1>=num2 and num1>=num3:
	largest=num1
elif num2>=num1 and num2>=num3:
	largest=num2
else:
	largest=num3
print("the largest number is:",largest)
