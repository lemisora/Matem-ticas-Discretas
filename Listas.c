//Descripción: Este programa se encarga de tratar matrices como listas (vectores), además de ofrecer la posibilidad de operar con las mismas como si de listas bidimensionales se tratara
//Nombre: Leonardo Michel Domingo Sánchez
//Fecha: 15-08-2023

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> //Biblioteca con funciones exclusivas para sistemas operativos compatibles con POSIX

int pd(int n, int i, int j){  //pd(),hace referencia a polinomio de direccionamiento
  //Esta función se encarga de realizar la conversión de una lista a una matriz para el entendimiento del usuario
  return (n*(j)+(i));         //Se regresa el índice de la lista que contiene el dato solicitado
}

void leeMatriz(int *L, int n, int m){    //Esta función realiza la lectura de la matriz y el almacenamiento de la misma en el vector (lista unidimensional)
  printf("\n");
  int i,j,k = 0;                        //Se inicializan las variables en 0
  for(i = 0;i < n;i++){                     
    for(j = 0;j < m;j++){
      printf("Ingrese el dato [%d , %d]: ",i+1,j+1);
      k = pd(n ,i ,j);                    //Se hace uso de la función polinomio de direccionamiento para cambiar el formato de índice de matriz al de una lista
      scanf("%d",&L[k]);                //Se realiza la lectura de datos de cada posición de la matriz
      fflush(stdin);                    //Se hace limpieza del buffer de entrada estándar para evitar la mayoría de problemas arraigados por el uso de scanf como método de entrada
    }
  }
}

void imprimeMatriz(int *L, int n, int m){ //Función que sirve para imprimir los datos de la matriz ingresada
  int i,j,k = 0; 
  for(i = 0;i < n;i++){
    if(j == m){
      printf("\n");
    }
    for(j = 0;j < m;j++){
      k = pd(n, i, j);
      printf("|%d| ",L[k]);
    }
  }
}

void pd_M(int *A, int *B, int n, int m){  //Función que sirve para calcular la suma de dos matrices
  int k = 0;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      k = pd(n, i, j);
      A[k] = A[k] + B[k];
    }
  }
}

void pd_MSTD(int *A, int *B, int n, int m){  //Función que sirve para calcular la matriz triangular superior derecha
  int k = 0;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      k =  pd(n, i, j);
      B[k] = A[k];
    }
  }
  for(int i = 0;i < n;i++){
    for(int j = 0;j < i;j++){
      k = pd(n, i, j);
      B[k] = 0;
    }
  }
}

int main(){

  printf("En este programa se opera con matrices, para comenzar deberá de introducir datos para operar con una a continuación\n");
  int n,m = 0, a = 0;

  printf("Ingrese n: ");
  scanf("%d",&n);
  printf("Ingrese m: ");
  scanf("%d",&m);
  
  system("clear");  //Las función system permite ejecutar un comando del sistema en el que se ejecuta el programa, en este caso se ejecuta "clear" para limpiar la pantalla, dicho comando solo se encuentra disponible para sistemas de tipo UNIX como Linux, BSD y macOS; aunque también existe dicha función en el intérprete de comandos de PowerShell
  usleep(600000);   //La función usleep es una función exclusiva para sistemas de tipo UNIX que permite detener la ejecución durante el tiempo en milisegundos que se haya ingresado

  int L[n*m];
  int L2[n*m];
  int L3[n*m];

  leeMatriz(L,n,m);
  usleep(600000);
  system("clear");

  while (a != 3) {
    printf("\n\n¿Qué desea calcular a continuación?\n\n");
    printf("\t1. La suma de la primer matriz con una segunda matriz del mismo tamaño\n");
    printf("\t2. La matriz triangular superior derecha de dicha matriz\n");
    printf("\t3. Salir\n");
    printf("\nIngrese su respuesta: ");
    scanf("%d",&a);

    switch (a) {
      case 1:
        usleep(600000); 
        system("clear");
        printf("A continuación ingrese los datos de la segunda matriz\n");
        leeMatriz(L2, n, m);
        usleep(600000);
        system("clear");
        pd_M(L, L2, n, m);
        printf("\nResultado de la suma de matrices: \n");
        imprimeMatriz(L, n, m);
        break; 
      case 2:
        usleep(600000);
        system("clear");
        pd_MSTD(L, L2, n, m);
        printf("\nResultado del cálculo de la matriz triangular superior derecha\n");
        imprimeMatriz(L2, n, m);
        break;
      case 3:
        printf("\n¡Fin del programa!\n");
        usleep(600000);
        system("clear");
        break;
    }
  }
  return 0;
}
