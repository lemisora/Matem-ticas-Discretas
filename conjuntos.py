import random

A=[0,0,0,0]
B=[0,0,0,0]
C=[0,0,0,0]
for i in range (0,4,1):
    A[i]=int(input("Ingrese un número para el conjunto A: "))
print("\n")
for i in range (0,4,1):
    B[i]=int(input("Ingrese un número para el conjunto B: "))

A =set( A )
B =set( B )

C=A |B
interseccion=A&B
difAB=A-B
difBA=B-A

print ( "\nArreglo A =" , A )
print ( "Arreglo B =" , B )
print ( "A Unión B =" , C )
print ( "Intersección =" , interseccion )
print ( "Diferencia A-B =" , difAB)
print ( "Diferencia B-A =" , difBA )