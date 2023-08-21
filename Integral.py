#Este programa calcula el área bajo la "curva" de una función lineal
#Esta función realiza los cálculos de la integral definida mediante los datos ingresados en la función principal

def f(fm,desde,div,deltax):
    area_parcial=0.0
    area_total=0.0
    for i in range(0,div,1):
        area_parcial=(((fm*(desde+i*deltax))+(fm*(desde+(i+1)*deltax)))*deltax)/2
        area_total=area_total+area_parcial
    return area_total

#Esta función calcula el área del triángulo basado en el valor de m y de b que son asignados en la función principal 
def altura_triangulo(fx,x):
    altura=fx*x
    return altura

#Se inicializa opc en S para que el ciclo mientras dé comienzo, y se inicializa cont en 0, este determina si será necesario seguir mostrando los datos importantes del funcionamiento de este programa al usuario
opc="S"
cont=0

#Se inicia un ciclo mientras que se detendrá hasta que el usuario desee salir del mismo oprimiendo la tecla N
while (opc!="N"):
    m=int(input("Ingrese el valor de m de la función lineal de forma (mx+b) con la que quiere trabajar \n"))

    #En el primer recorrido del ciclo se le muestran al usuario ciertos datos importantes acerca del funcionamiento de este programa
    if cont==0:
        print("\nPara la integral del área a calcular \n - A es el valor de x desde el que se calcula \n - B es el valor de x hasta el que se calcula \n - N es el número de divisiones en que se dividirá el intervalo A-B para una mejor aproximación\n")
    
    #Se solicita al usuario ingresar los valores que se conocen para el cálculo del área
    a=int(input("Ingrese el valor de a: \n"))
    b=int(input("Ingrese el valor de b: \n"))
    n=int(input("Ingrese el valor de n: \n"))
    Dx=(b-a)/n
    
    #Se hacen llamados a los módulos definidos al inicio para facilitar el uso con distintas funciones lineales
    funcionarea=f(m,a,n,Dx)
    funciontriangulo=altura_triangulo(m,b)
    areatriangulo=((b-a)*funciontriangulo)/2

    #Se imprimen los resultados finales para comparar las áreas obtenidas mediante dos métodos distintos, el de la integral y el del cálculo del valor de un triángulo
    print("El área bajo la curva es: ",funcionarea)
    print("El área comprobada mediante un triángulo es: ",areatriangulo)
    cont=cont+1

    opc=str(input("Oprima la tecla s para continuar, de lo contrario presione N [s/N]\n"))
