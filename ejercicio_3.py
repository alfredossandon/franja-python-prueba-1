#3) Escribir un programa que haga transformaciones de pesos a dólares. Debe preguntarle al usuario si desea transformar 
# de pesos mexicanos a dólares, de pesos chilenos a dólares, o desde pesos argentinos a dólares. 
# Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió 

#Peso Chileno a dolar: 855
#Peso Mexicano a dolar: 20
#Peso Argentino a dolar: 115

mex = 1
chi = 2
arg = 3

mexicodolar = 20
chiledolar = 855
argentinadolar = 115

monedas = int(input("Ingrese cuantas monedas quiere cambiar a dolares: "))

eleccion = int(input("Ingrese la divisa que quiere cambiar a dolares 1 Mex, 2 Chi y 3 Arg: "))
if eleccion == 1 :
    cambiomexico = (monedas / mexicodolar)
    print(cambiomexico)
elif eleccion == 2 :
    cambiochile = (monedas / chiledolar)
    print(cambiochile)
if eleccion == 3 :
    cambioargentina = (monedas / argentinadolar)
    print(cambioargentina)
    