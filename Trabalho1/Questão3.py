from scipy.fft import fft2
from sympy import diff, symbols


x, y, z = symbols('x y z')

def f1(x,y,z):
    c=x**2+x*y+z**2-12
    return c

def f2(x,y,z):
    c=x-y*z-10
    return c

def f3(x,y,z):
    c=2*x**2-y**2+z**2+5
    return c

def fx1(x1,x2,x3,derivar):
   a=diff(x**2+x*y+z**2-12,derivar)
   resultado=a.subs({
  x: x1,
  y: x2,
  z: x3

    })

   return resultado

def fx2(x1,x2,x3,derivar):
   a=diff(x-y*z-10,derivar)
   resultado=a.subs({
  x: x1,
  y: x2,
  z: x3

    })

   return resultado
   
def fx3(x1,x2,x3,derivar):
   a=diff(2*x**2-y**2+z**2+5,derivar)
   resultado=a.subs({
  x: x1,
  y: x2,
  z: x3

    })

   return resultado

e=10**-4
b=[[1],[1],[1]]
aux1=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,2):

  F=[[f1(b[0][0],b[1][0],b[2][0])],[f2(b[0][0],b[1][0],b[2][0])],[f3(b[0][0],b[1][0],b[2][0])]]
  J=[[fx1(b[0][0],b[1][0],b[2][0],x),fx1(b[0][0],b[1][0],b[2][0],y),fx1(b[0][0],b[1][0],b[2][0],z)],[fx2(b[0][0],b[1][0],b[2][0],x),fx2(b[0][0],b[1][0],b[2][0],y),fx2(b[0][0],b[1][0],b[2][0],z)],[fx3(b[0][0],b[1][0],b[2][0],x),fx3(b[0][0],b[1][0],b[2][0],y),fx3(b[0][0],b[1][0],b[2][0],z)]]

  for i in range(len(J)):
      for l in range(len(J)):
        aux1[i][l]=(J[i][l]*-1)   

  Gauss(aux1,F)   #executar questão 1 
  y=Sol(J,F)    #executar questão 1

  for i in range(len(b)):
    b[i][0]+=y[i]

for i in range(len(y)):
  print(y[i])

print('\n\n')

for i in range(len(b)):
  print(b[i][0])  
