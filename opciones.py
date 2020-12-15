#Importamos paquetes
import numpy as np
import sympy as sp
#funcion que busca maximos de forma numerica
def max(x=np.array([]),y=np.array([])):
    lx=len(x)
    maxi = np.array([])
    pxmx = np.array([])
    i = 1
    maxi = np.append(maxi,y[0])
    pxmx = np.append(pxmx,x[0])
    j=0
    while i <= (lx-1):
        if y[i] > maxi[0]:
            if len(maxi) > 1:
                maxi = np.array([])
                pxmx = np.array([])
                maxi = np.append(maxi,y[i])
                pxmx = np.append(pxmx,x[i])
                j=0
            else:
                maxi[0]=y[i]
                pxmx[0]=x[i]
        elif round(y[i],3) == round(maxi[j],3):
            maxi = np.append(maxi,y[i])
            pxmx = np.append(pxmx,x[i])
            j=j+1
        i=i+1
    return maxi,pxmx

#funcion que busca minimos de forma numerica
def min(x=np.array([]),y=np.array([])):
    lx=len(x)
    mini = np.array([])
    pxmn = np.array([])
    i = 1
    mini = np.append(mini,y[0])
    pxmn = np.append(pxmn,x[0])
    j=0
    while i <= (lx-1):
        if round(y[i],2) < round(mini[0],2):
            if len(mini) > 1:
                mini = np.array([])
                pxmn = np.array([])
                mini = np.append(mini,y[i])
                pxmn = np.append(pxmn,x[i])
                j=0
            else:
                mini[0]=y[i]
                pxmn[0]=x[0]
        elif round(y[i],2) == round(mini[0],2):
            mini = np.append(mini,y[i])
            pxmn = np.append(pxmn,x[i])
            j=j+1
        i=i+1
    return mini,pxmn

#funcion que busca el valor más proximo de forma numerica
def valor(x,y,d):
    f=eval(d)         
    lx=len(x)
    vxmc = np.array([])
    vymc = np.array([])
    dm = np.abs(f-y[0])
    vxmc = np.append(vxmc,x[0])
    vymc = np.append(vymc,y[0])
    i=1
    while(i <= (lx-1)):
        d = np.abs(f-y[i])
        if d < dm:
            if len(vymc)> 1:
                vxmc = np.array([])
                vymc = np.array([])
                vxmc = np.append(vxmc,x[0])
                vymc = np.append(vymc,y[0])
                dm = d

            else:
                vymc[0]=y[i]
                vxmc[0]=x[i]
                dm = d
        elif d == 0:
            vymc[0]=y[i]
            vxmc[0]=x[i]
            dm=d
        elif d == dm:
                vxmc = np.append(vxmc,x[0])
                vymc = np.append(vymc,y[0])
        i=i+1            
    return f,vxmc,vymc,dm

def Simpcomp(a,b,n,x,y,h):
    hsp = h/3
    I = np.sum(y[1:-1:2])
    P = np.sum(y[2:-1:2])
    integral = (hsp)*(y[0]+4*I+2*P+y[-1])
    return integral

def Intesimpson(a,b,err,expresion,Xrr,y):
    Tol = 10**(-err)
    error = 100
    x = sp.Symbol('x',real=True)
    f = sp.lambdify([x],expresion,'numpy')
    f1 = sp.lambdify([x],(sp.diff(f(x),x)),'numpy')
    f2 = sp.lambdify([x],(sp.diff(f1(x),x)),'numpy')
    f3 = sp.lambdify([x],(sp.diff(f2(x),x)),'numpy')
    f4 = sp.lambdify([x],(sp.diff(f3(x),x)),'numpy')
    ArregloM4 = f4(Xrr)
    print(ArregloM4)
    M4 = np.max(ArregloM4)
    n = 1    
    while error > Tol:
        error = (((b-a)**5)/(180*(n**4)))*M4
        print(error)
        print(Tol)
        n = n+1
    if (n%2)==1:
        n=n+1
    h = (b-a)/n
    IneSimp = Simpcomp(a,b,n,x,y,h)
    return error,IneSimp,n

