
def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def div(num1,num2):
    return(num1/num2)
def mul(num1,num2):
    return(num1*num2)

print("1-add .")
print("2-Subtract.")
print("3-devide .")
print("4-multplie.")

z=input("choose number of pocess :")
x=float(input("enter 1st number"))
y=float(input("enter 2nd number"))
if z=='1':
    print(x, "+", y, "=",add(x,y))
elif z=='2':
    print(x, "-", y, "=",sub(x,y))
elif z=='3':
    print(x, "/", y, "=",div(x,y))
elif z=='4':
    print(x, "*", y, "=",mul(x,y))
else:
    print("error")   
