n = (input("Enter a number: "))
sum = 0
for i in n:
    i = int(i)
    cube = i**3
    sum = sum + cube
if sum == int(n):
    print("This is a Amstrong number")
else:
    print("Not a Amstrong number")