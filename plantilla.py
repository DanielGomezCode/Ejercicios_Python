#Las preguntas que te irá haciendo la esfinge corresponden a los print de esta plantilla
#Por favor completa cada reto

#Clase 1 Proyecto: Definidendo la aventura

#Reto 1 - Pon tu respuesta después del print
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

mapa = 50
botas = 40
bateria = 25
linterna = 40
agua = 50
botella = 25
snacks = 10
brujula = 50
reloj = 50
lentes_sol = 20


#Reto 2 - Pon tu respuesta después de cada print
print("Lista tres objetos del equipamiento: Nombre y valor")
print("brujula", brujula)
print("botas", botas)
print("lentes_sol", lentes_sol)



print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

linterna_funcional = linterna + bateria
agua_en_botella = agua + botella
ropa_ligera = lentes_sol + botas
reloj_funcional = reloj + bateria

print("ropa ligera", ropa_ligera)
print("reloj funcional", reloj_funcional)
print("agua en botella", agua_en_botella)
print("linterna_funcional", linterna_funcional)


print("¿El precio del agua en botella es menor al de la linterna funcional?")

print(agua_en_botella < linterna_funcional)



print("¿Cuanto valdría comprar unos snacks y una brujula?")

print(snacks + brujula)



print("¿Si tienes 100 puntos, te alcanza para comprar unas botas?")

print(botas <= 100)




#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("La esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")

mochila = 0

if agua + brujula + botella + bateria + mapa <= 200:
    mochila = agua + brujula + botella + bateria + mapa
    print("El valor de los elementos es menor a 200: ", mochila)

elif reloj + mapa + brujula + botas <= 200:
    reloj = mapa + brujula + botas 
    print("El valor de los elementos es menor a 200", mochila)

else:
    print("Ups! Ninguna de tus intentos fue exitoso")

if agua_en_botella + linterna_funcional + brujula <= 200:
    mochila = agua_en_botella + linterna_funcional + brujula
    print("El valor de los elementos es menor a 200. Total compra: ", mochila)




#Reto 4 - Pon tu respuesta después del print
print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")

mochila_dos = 0

while (mochila_dos <= 200):
    mochila_dos += agua_en_botella
    print("Mochila dos: ", mochila_dos)


#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")









#Reto 5 - Pon tu respuesta después del print
print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")











#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")

