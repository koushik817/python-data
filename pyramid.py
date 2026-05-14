A=int(input("Enter Number:"))
spaces=" "
stars="*"
for i in range(A):
 print(spaces*(A-i-1)+stars*(2*i+1))
