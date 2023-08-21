a=int(input("Ingresa el valor de A: "))
b=int(input("Ingresa el valor de B: "))
c=a%b
if(c==0):
    print("El máximo común divisor es: ",b)
while (c!=0):
    c=a%b
    if (c==0):
        print("El máximo común divisor es: ", b)
    else:
        a=b
        b=c