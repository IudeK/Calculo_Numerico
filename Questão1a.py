from http.client import OK
from logging import CRITICAL
import math


x= int(input('Digite a ordem de sua matriz: '))

y=x+1
m=[]
A=[]
b=[]

def CriaMatriz(linha,coluna):
    lista=[]
    for i in range(0,linha):
         l = []
         for j in range(0,coluna):
           l.append(0)
         lista.append(l)  
    return lista     
     
m=CriaMatriz(x,y)
A=CriaMatriz(x,y-1)
b=CriaMatriz(x,1)

for i in range(0,x):
    for j in range(0,y):
        print("Digite o valor para a linha " +str(i)+ " coluna " +str(j))
        m[i][j]=float(input())



for i in range(0,x):
    b[i][0]=m[i][y-1]
    for j in range(0,y-1):    
            A[i][j]=m[i][j]
 
        
print("\n" * 130)
print('\nMatriz digitada:\n')
for i in range(0,x):
    for j in range(0,y):
        print(f'[{m[i][j]}]', end='')
        
    print()

print('\n************\n\nMatriz A: \n')

for i in range(0,x):
    for j in range(0,y-1):            
        print(f'[{A[i][j]}]', end='')
    print()

print('\nMatriz b: \n')        
for i in range(0,x):
     print(f'[{b[i][0]}]', end='')
     print()

print()

def GaussPivoteamento(A,b):
    for i in range(len(A)):
        pivo=math.fabs(A[i][i])
        linhaPivo = i
        for j in range(i+1,len(A)):
            aux =math.fabs(A[j][i])
            if aux>pivo:
                pivo=aux
                linhaPivo=j
        if linhaPivo!=i:
            auxA=A[i]
            A[i]=A[linhaPivo]
            A[linhaPivo]=auxA

            auxB=b[i][0]
            b[i][0]=b[linhaPivo][0]
            b[linhaPivo][0]=auxB
        
        for k in range(i+1,len(A)):
            multiplicador = A[k][i]/A[i][i] 
            for l in range(i,len(A)):
                A[k][l]-= multiplicador*A[i][l]
            b[k][0]-= multiplicador*b[i][0]


GaussPivoteamento(A,b)

print('\n************\n\nMatriz A Escalonada: \n')

for i in range(0,x):
    for j in range(0,y-1):            
        print(f'[{A[i][j]}]', end='')
    print()

print('\nMatriz b Escalonada: \n')        
for i in range(0,x):
     print(f'[{b[i][0]}]', end='')
     print()

print()