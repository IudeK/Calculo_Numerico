import numpy as np

m =[[9,-2,1,3,1,0],[1,-1,2,6,1,2],[2,-3,7,1,0,1],[1,6,-1,4,2,1],[1,-2,2,1,8,2]]
#m =[[8,2,-1,0,1],[2,-4,0,0,1],[0,-2,8,-1,1],[-0,0,-1,4,1]]

def CriaMatriz(linha, coluna):
    lista = []
    for i in range(linha):
        l = []
        for j in range(coluna):
            l.append(0)
        lista.append(l)
    return lista

for i in range (len(m)):
        for j in range(len(m)+1):
            print(f'[{m[i][j]}]', end='')
        print()            

A = CriaMatriz(len(m), len(m)) 
b = CriaMatriz(len(m), 1)        

print()
for i in range(0, len(m)):
    b[i][0] = m[i][len(m)]
    for j in range(0,len(m)):
        A[i][j] = m[i][j]

def distRelativa(vetorP,vetorAux)  :
    n = np.size(vetorP)
    aux2 = np.zeros(n)
    aux3 = np.zeros(n)
    a= 0
    b= 0
    for i in range(0,n):
        aux2[i]= vetorP[i]-vetorAux[i] 
        aux3[i]= vetorP[i]
        if aux2[i]<0:
            aux2[i]*=-1
        if aux3[i]<0:
            aux3[i]*=-1
    a=max(aux2) 
    b=max(aux3)
    a/=b
    return a

def gaussSeidel(A,b,y):
    n = np.size(b)
    aux = np.zeros(n)
    controle=100
    count=0

    while count<4:#controle>10**-4:
        for i in range(len(A)):
            x=b[i][0]
            for j in range(len(A)):
                if i!=j:
                    x-=A[i][j]*y[j]
            x/=A[i][i]
            y[i]=x    
        count+=1
        #controle=distRelativa(y,aux)
        for i in range(len(aux)):
            aux[i]=y[i]    

    print('\n'+str(count)+' repetições')         

n = np.size(b)
y = np.zeros(n)                      
gaussSeidel(A,b,y)  

for i in range (len(y)):
    print(f'[{y[i]}]', end='')