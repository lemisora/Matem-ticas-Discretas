def fact(j):
    fact=1
    i=1
    while(i<=j):
        fact=fact*i
        i=i+1
    return fact

n=int(input("Ingrese el valor de n: "))
r=int(input("Ingrese el valor de r: "))

opc=int(input("¿Qué desea hacer?\n\t0.Salir\n\t1.Combinación\n\t2.Permutación\n\n\t"))
perm=fact(n)
perm1=fact(n-r)
permuta=perm/perm1
while(opc!=0):
    if(opc==1):
        com=fact(r)
        combina=perm/(perm1*com)
        print("El número de combinaciones posibles es de: ",combina)
        opc=0
    if(opc==2):
        print("El número de permutaciones posibles es de: ", permuta)
        opc=0
    
print("Final del programa")