def mcd(a,b):
	c=a%b
	while(c!=0):
		c=a%b
		if(c!=0):
			a=b
			b=c
	return b

prim=int(input("Ingresa el valor de A: "))
seg=int(input("Ingresa el valor de B: "))
MCM=(prim*seg)/mcd(prim,seg)
print("El mínimo comúm multiplo es: ",MCM)