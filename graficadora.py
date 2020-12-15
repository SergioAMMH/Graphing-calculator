#importamos libreria
import validador as val
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sympy import *
import opciones as op

#Creamos la ventana
Graficadora = tk.Tk()
#Definimos su nombre
Graficadora.title("Graficadora")
#Añadimos icono
Graficadora.iconbitmap("icono.ico")
#Definimos redimensionalidad
Graficadora.resizable(0,0)
#Definimos las dimensiones
Graficadora.geometry("375x225")
#definimos función para ventana instrucciones
def venins():
    instructivo= tk.Tk()
    instructivo.title("Instrucciones para usar la graficadora")
    instructivo.iconbitmap("Instrucciones.ico")
    instructivo.resizable(0,0)
    instructivo.geometry("450x600")
    instructivo.config(bg='white')
    etiquetains1=tk.Label(instructivo,text='Instrucciones:',bg='white')
    etiquetains1.pack(anchor=tk.NW)
    etiquetains2=tk.Label(instructivo,text='1.-Debe introducir la expresión para su función en el primer recuadro.',bg='white',fg='black')
    etiquetains2.pack(anchor=tk.NW)
    etiquetains3=tk.Label(instructivo,text="2.-a es el inicio del intervalo donde quiere graficar la función",bg='white',fg='black')
    etiquetains3.pack(anchor=tk.NW)
    etiquetains4=tk.Label(instructivo,text="3.-b es el fin del intervalo donde quiere graficar la función   ",bg='white',fg='black')
    etiquetains4.pack(anchor=tk.NW)
    etiquetains5=tk.Label(instructivo,text="4.-Al presionar max graficará los maximos relativos en el intervalo.",bg='white',fg='black')
    etiquetains5.pack(anchor=tk.NW)
    etiquetains6=tk.Label(instructivo,text="5.-Al presionar min graficará los minimos relativos en el intervalo.",bg='white',fg='black')
    etiquetains6.pack(anchor=tk.NW)
    etiquetains7=tk.Label(instructivo,text="6.-al presionar Integral se realizará la integral númerica.         ",bg='white',fg='black')
    etiquetains7.pack(anchor=tk.NW)
    etiquetains8=tk.Label(instructivo,text="7.-Al presionar f(x)=d, usted introduce una d y se busca el valor proximo.",bg='white',fg='black')
    etiquetains8.pack(anchor=tk.NW)
    etiquetains9=tk.Label(instructivo,text='Las operaciones validas para instroducir en la graficadora son:  ',bg='white',fg='black')
    etiquetains9.pack(anchor=tk.NW)
    etiquetains10=tk.Label(instructivo,text='a) para suma tecle: +',bg='white',fg='black')
    etiquetains10.pack(anchor=tk.NW)
    etiquetains11=tk.Label(instructivo,text='b) para resta tecle: -',bg='white',fg='black')
    etiquetains11.pack(anchor=tk.NW)
    etiquetains12=tk.Label(instructivo,text='c) para potencia tecle: **',bg='white',fg='black')
    etiquetains12.pack(anchor=tk.NW)
    etiquetains13=tk.Label(instructivo,text='d) para raíz cuadrada tecle: sqrt',bg='white',fg='black')
    etiquetains13.pack(anchor=tk.NW)
    etiquetains14=tk.Label(instructivo,text='e) para seno tecle: sin(--)',bg='white',fg='black')
    etiquetains14.pack(anchor=tk.NW)
    etiquetains15=tk.Label(instructivo,text='f) para coseno tecle: cos(--)',bg='white',fg='black')
    etiquetains15.pack(anchor=tk.NW)
    etiquetains16=tk.Label(instructivo,text='g) para tangente tecle: tan(--)',bg='white',fg='black')
    etiquetains16.pack(anchor=tk.NW)
    etiquetains17=tk.Label(instructivo,text='h) para cotangente tecle: cot(--)',bg='white',fg='black')
    etiquetains17.pack(anchor=tk.NW)
    etiquetains18=tk.Label(instructivo,text='i) para secante tecle: sec(--)',bg='white',fg='black')
    etiquetains18.pack(anchor=tk.NW)
    etiquetains19=tk.Label(instructivo,text='j) para cscante tecle: csc(--)',bg='white',fg='black')
    etiquetains19.pack(anchor=tk.NW)
    etiquetains20=tk.Label(instructivo,text='k) para el valor pi tecle: pi',bg='white',fg='black')
    etiquetains20.pack(anchor=tk.NW)
    etiquetains21=tk.Label(instructivo,text='l) para funcion exponencial tecle: exp(--)',bg='white',fg='black')
    etiquetains21.pack(anchor=tk.NW)
    etiquetains22=tk.Label(instructivo,text='m) para agrupar terminos y operaciones utilice ()',bg='white',fg='black')
    etiquetains22.pack(anchor=tk.NW)
    etiquetains23=tk.Label(instructivo,text='Nota 1: debe marcar la multiplicacion antes de un parentesis *(--)',bg='white',fg='black')
    etiquetains23.pack(anchor=tk.NW)
    etiquetains24=tk.Label(instructivo,text='Nota 2: la función debe instroducirse en terminos de x',bg='white',fg='black')
    etiquetains24.pack(anchor=tk.NW)
    etiquetains25=tk.Label(instructivo,text='Nota 3: Para poder evaluar la función debe cerrar todos los parentesis que abra',bg='white',fg='black')
    etiquetains25.pack(anchor=tk.NW)
    etiquetains26=tk.Label(instructivo,text='Nota 4: cualquier operador distinto a los listados no será valido',bg='white',fg='black')
    etiquetains26.pack(anchor=tk.NW)

    instructivo.mainloop
def fungraficadora():
    #Cadenas de texto
    vacia=''
    iniciotxt = 'El dato introducido'
    nonum= 'no es un numero'
    etiquetavalidadora["text"] = vacia
    
    #obtenemos la expresión
    expr = expresion.get()
    ainter = ava.get()
    binter = bva.get()
    oppunto = punto.get()
    opintegral = Integralva.get()
    #convertimos el texto a minusculas
    expr1 = expr.lower()
    if len(expr1 )== 0:
        etiquetavalidadora['text']='No se introdujo una expresión f(x)' 
        return
    valexpr = val.exprvalidador(expr1)
    #validador escritura de f(x)
    if valexpr == False:
        txt = val.valexpr(expr1)
        etiquetavalidadora['text']=txt
        return

    #informamos de posible error en a
    av = val.validador(ainter)
    if av == False:
        if len(ainter)==0:
            etiquetavalidadora['text']='No se introdujo un valor a'   
        else:
            anonum = iniciotxt +' a '+nonum
            etiquetavalidadora['text']=anonum
        return
    bv = val.validador(binter)
    if  bv == False:
        if len(binter)==0:
            etiquetavalidadora['text']='No se introdujo un valor b'   
        else:
            bnonum = iniciotxt +' b '+nonum
            etiquetavalidadora['text']=bnonum
        return        

    if oppunto == True:
        puntop = dva.get()
        dv = val.validador(puntop)
        if dv == False:
            if len(puntop)==0:
                etiquetavalidadora['text']='No se introdujo un valor d'   
            else:
                pnonum = iniciotxt +' d '+nonum
                etiquetavalidadora['text']=pnonum
            return
        else:
            dint = eval(puntop)

    if  opintegral == True:
        error = intva.get()
        errv = val.validadorint(error)
        if errv == False:
            if len(error)==0:
                etiquetavalidadora['text']='No se introdujo error'   
            else:
                pnonum = iniciotxt +' en error '+nonum
                etiquetavalidadora['text']=pnonum
            return
        else:
            errvalor = eval(error)
    #Definimos valores para graficar
    a = eval(ainter)
    b = eval(binter)
    ylatex = latex(sympify(expr1))
    if a>b:
        atemp = a
        a=b
        b=atemp
    cint = int((np.abs(a-b))/0.007)
    if cint > 1000:
        cint = 1000
        X = np.linspace(a,b,cint)
    else:
        X=np.linspace(a,b,1000)
    lx = len(X)
    y = np.array([])
    i = 0
    while i <= (lx-1) :
        x = float(X[i])
        loc = {'sqrt': sqrt, 'sin': sin, 'cos': cos, 'tan': tan,'cot':cot, 'x':x,'sec':sec,'csc':csc ,'pi':np.pi, 'exp':np.exp}
        y = np.append(y,eval(expr1, loc))
        i = i+1
    omax = bmaxi.get()
    omin = bmini.get()
    #inicio ventana grafica
    grafica = tk.Tk()
    def opguardar():
        nombrefig = nombre.get()
        fig1.savefig('{0}'.format(nombrefig))
        return

    #definimos titulo
    grafica.title("Grafica {0}".format(expr1))
    #Añadimos icono
    grafica.iconbitmap("icono.ico")
    #Definimos redimensionalidad
    #grafica.resizable(0,0)
    #Definimos las dimensiones
    grafica.geometry("600x400")
    #Etiquetas y entradas
    bguardar = tk.Button(grafica,text='Guardar',bg = 'Blue',fg='white',command=opguardar)
    bguardar.pack(padx=1,pady=1,ipadx=1,ipady=1)
    nombre = tk.StringVar()
    nombregrafica = tk.Entry(grafica,width=50,textvariable=nombre)
    nombregrafica.pack(padx=1,pady=1,ipadx=1,ipady=1)
    label = tk.Label(grafica)
    label.pack(padx=1,pady=1,ipadx=1,ipady=1)
    fig1 = matplotlib.figure.Figure(figsize=(10,5),dpi=100)
    ax = fig1.add_subplot(111)
    ax.plot(X,y, c='k', ls= '-',label=(r'${0}$'.format(ylatex)))
    if omax == True:
        #obtenemos maximos de forma númerica
        maxi,mxpx = op.max(X,y)
        #graficamos maximos
        ax.plot(mxpx, maxi,'ro', label = r'maximos')
    if omin ==True:
        #obtenemos minimos
        mini,mnpx = op.min(X,y)
        #graficamos minimos
        ax.plot(mnpx,mini,'bo', label = r'minimos')
    if oppunto == True:
        va,dmx,dmy,d = op.valor(X,y,puntop)
        #valor es igual
        if d == 0 :
            ax.axhline(y=va, xmin=0, xmax=1, color='g', ls="--", label=r'valor a buscar')
            ax.plot(dmx,dmy,'co', label=r'puntos cercanos')
        else:
            if len(dmx)>1:
                ax.axhline(y=va, xmin=0, xmax=1, color='g', ls="--", label=r'valor a buscar')
                ax.plot(dmx,dmy,'co', label=r'puntos cercanos')
            else:
                ax.axhline(y=va, xmin=0, xmax=1, color='g', ls="--", label=r'valor a buscar')
                ax.plot(dmx,dmy,'co', label=r'punto cercano')
    if opintegral == True:
        error,numintegracion, n = op.Intesimpson(a,b,errvalor,expr1,X,y)
        x = Symbol('x',real=True)
        f = lambdify([x],expr1,'numpy')
        label['text']='Integral = {0} con n={1}, con error {2}'.format(numintegracion,n,error)
        #eje x
        ax.axhline(0, color='g', ls="--")
        #intervalo de integración
        ax.axvline(a, color='r', ls="dotted")
        ax.axvline(b, color='r', ls="dotted")
        #Area sombreada
        ax.fill_between(X, f(X),
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2) 

    ax.legend(loc='upper left')
    fig1.align_xlabels
    canvas = FigureCanvasTkAgg(fig1, grafica)
    canvas.get_tk_widget().pack(fill=tk.X,side=tk.TOP)
    canvas._tkcanvas.pack(fill=tk.X,side=tk.TOP)

    canvas.draw()
    grafica.mainloop()
    return

def puntod():
    oppunto = punto.get()
    if(oppunto == True):
        etiqueta4 = tk.Label(Graficadora,text='d')
        etiqueta4.grid(padx=1,pady=1,row=4,column=0,columnspan=1)
        dvalor = tk.Entry(Graficadora,width=50,textvariable=dva)
        dvalor.grid(padx=1,pady=1,row=4,column=1,columnspan=5)

def error():
    opintegral = Integralva.get()
    if(opintegral == True):
        etiquetaint = tk.Label(Graficadora,text='10**-')
        etiquetaint.grid(padx=1,pady=1,row=5,column=0,columnspan=1)
        intvalor = tk.Entry(Graficadora,width=50,textvariable=intva)
        intvalor.grid(padx=1,pady=1,row=5,column=1,columnspan=5)


#INICIO DE PARTES DE LA VENTANA PRINCIPAL
Instrucciones = tk.Button(Graficadora,text='Instrucciones',bg = 'Blue',fg='white',command=venins)
Instrucciones.grid(padx=1,pady=1,row=0,column=1,columnspan=3)

#etiqueta  fx
fx = tk.Label(Graficadora,text='f(x)')
fx.grid(padx=1,pady=1,row=1,column=0,columnspan=1)
#Creamos la caja de texto
expresiontxt = tk.StringVar()
expresion = tk.Entry(Graficadora,width=50,textvariable=expresiontxt)
expresion.grid(padx = 1,pady=1,row=1,column=1,columnspan=5)

#Valores
ava = tk.StringVar()
etiqueta2 = tk.Label(Graficadora,text='a')
etiqueta2.grid(padx=1,pady=1,row=2,column=0,columnspan=1)
avalor = tk.Entry(Graficadora,width=50,textvariable=ava)
avalor.grid(padx=1,pady=1,row=2,column=1,columnspan=5)

bva = tk.StringVar()
etiqueta3 = tk.Label(Graficadora,text='b')
etiqueta3.grid(padx=1,pady=1,row=3,column=0,columnspan=1)
bvalor= tk.Entry(Graficadora,width=50,textvariable=bva)
bvalor.grid(padx=1,pady=1,row=3,column=1,columnspan=5)
#valor para punto d
dva=tk.StringVar()

#valor error
intva = tk.StringVar()

#valores a:
bmaxi = tk.BooleanVar()
btmaxi = tk.Checkbutton(Graficadora,text='max',variable=bmaxi)
btmaxi.grid(padx=1,pady=1,row=6,column=0,columnspan=1)

bmini = tk.BooleanVar()
btmini = tk.Checkbutton(Graficadora,text='min',variable=bmini)
btmini.grid(padx=1,pady=1,row=6,column=1,columnspan=1)

Integralva = tk.BooleanVar()
Integralb = tk.Checkbutton(Graficadora,text='Integral',variable=Integralva,command = error)
Integralb.grid(padx=1,pady=1,row=6,column=2,columnspan=1)

punto = tk.BooleanVar()
bpunto= tk.Checkbutton(Graficadora,text='f(x)=d',variable=punto,command = puntod)
bpunto.grid(padx=1,pady=1,row=6,column=3,columnspan=1)

#Boton graficar
bgraficar = tk.Button(Graficadora,text='Graficar',bg='blue',fg='white',command = fungraficadora)
bgraficar.grid(padx=1,pady=1,row=7,column=2,columnspan=1)
etiquetavalidadora = tk.Label(Graficadora)
etiquetavalidadora.grid(padx=1,pady=1,row=8,column=1,columnspan=3)


Graficadora.mainloop()