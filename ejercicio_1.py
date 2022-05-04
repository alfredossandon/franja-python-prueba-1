#1) Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento 
#del 60%. Escribe un programa que comience leyendo el número de barras vendidas que no son del día. 
#Después tu programa debe mostrar el precio habitual de una barra de pan, 
#el descuento que se le hace por no ser fresca y el coste final total.

pandeldia = 3.49
pannofresco = 2.09
print("El precio de una barra de pan fresco es de 3.49€ y en descuento por no ser del dia es del 60 por ciento")

pananejo = float(input("Ingrese la cantidad de barras de pan que no son del dia: "))
print("Su precio final es: ")
print(pannofresco*pananejo)
