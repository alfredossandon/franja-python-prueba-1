#Escribir un programa que le pregunte al usuario una cantidad a invertir, el interés porcentual anual 
#y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales.

inversion = float(input("Ingrese la cantiad a invertir: "))

interespanual = float(input("Ingrese el interes porcentual anual: "))

años = float(input("Ingrese la cantidad de años a pagar: "))

capitalfinal = inversion * ((interespanual / 100) + 1 ) ** años

print("Su Capital Final obtenido es: ")

print(round(capitalfinal,2))
